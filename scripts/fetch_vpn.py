#!/usr/bin/env python3

import base64
import json
import random
import re
import socket
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone


TIMEOUT = 8
MAX_WORKERS = 30
MAX_CONFIGS = 500

SOURCES = [
    # igareck — Russia-specific sources
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Vless-Reality-White-Lists-Rus-Mobile.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_SS+All_RUS.txt",

    # Barry Far — corrected repository name: V2ray-Config
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vmess.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/trojan.txt",

    # Other public aggregators
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity.txt",
    "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub",
    "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt",
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt",

    # Additional active public source
    "https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/main/splitted-by-protocol/vless.txt",
]


VALID_PREFIXES = (
    "vless://",
    "vmess://",
    "ss://",
    "trojan://",
    "hysteria2://",
    "hy2://",
    "tuic://",
    "wireguard://",
)


def fetch_url(url):
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
        )

        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()

        # Some public subscription files are base64 encoded.
        try:
            decoded = base64.b64decode(
                raw + b"==",
                validate=False,
            ).decode("utf-8", errors="ignore")

            if any(p in decoded for p in VALID_PREFIXES):
                return decoded
        except Exception:
            pass

        return raw.decode("utf-8", errors="ignore")

    except Exception as exc:
        print(
            f"  [SKIP] {url[:100]}... → {exc}",
            file=sys.stderr,
        )
        return ""


def extract_configs(text):
    clean_lines = []

    for raw_line in text.splitlines():
        # Никогда не пропускаем NUL / управляющие бинарные символы
        # в опубликованные subscription-файлы.
        line = raw_line.replace("\x00", "").strip()

        if not line:
            continue

        if any(line.startswith(prefix) for prefix in VALID_PREFIXES):
            # Конфиг должен быть обычной UTF-8 строкой.
            clean_lines.append(line)

    return clean_lines


def parse_host_port(config):
    """
    Try to extract host/port from common proxy URI formats.

    This is only a TCP reachability check.
    It does NOT prove that the VPN protocol itself works.
    """

    try:
        # VMess is commonly base64 encoded JSON.
        if config.startswith("vmess://"):
            payload = config[8:].split("#", 1)[0]
            data = base64.b64decode(
                payload + "==",
                validate=False,
            ).decode("utf-8", errors="ignore")

            obj = json.loads(data)

            host = obj.get("add")
            port = obj.get("port", 443)

            if host and str(port).isdigit():
                return host, int(port)

        parsed = urllib.parse.urlparse(config)

        host = parsed.hostname
        port = parsed.port

        if host and port:
            return host, port

        # Fallback for unusual SS formatting.
        if config.startswith("ss://"):
            body = config[5:].split("#", 1)[0]

            if "@" in body:
                candidate = body.rsplit("@", 1)[1]

                if ":" in candidate:
                    host_part, port_part = candidate.rsplit(":", 1)

                    if port_part.isdigit():
                        return host_part.strip("[]"), int(port_part)

    except Exception:
        pass

    return None, None


def check_config(config):
    host, port = parse_host_port(config)

    if not host or not port:
        return False

    try:
        with socket.create_connection(
            (host, port),
            timeout=TIMEOUT,
        ):
            return True
    except Exception:
        return False


RU_CIDR_SOURCE = (
    "https://raw.githubusercontent.com/"
    "igareck/vpn-configs-for-russia/main/WHITE-CIDR-RU-all.txt"
)


def count_configs(path):
    """Количество валидных непустых строк-конфигов без grep."""
    count = 0

    with open(path, "r", encoding="utf-8", errors="strict") as file:
        for line in file:
            line = line.strip()

            if line and not line.startswith("#"):
                count += 1

    return count


def clean_config_file(path):
    """
    Приводит текстовый subscription-файл к чистому UTF-8:
    удаляет NUL и управляющие символы из содержимого строк.
    """
    p = Path(path)

    raw = p.read_bytes()

    # UTF-8 с заменой потенциально испорченных последовательностей.
    text = raw.decode("utf-8", errors="replace")

    # Удаляем NUL.
    text = text.replace("\x00", "")

    # Удаляем остальные ASCII control chars, кроме TAB/LF/CR.
    text = "".join(
        ch for ch in text
        if ch in "\t\n\r" or ord(ch) >= 32
    )

    p.write_text(text, encoding="utf-8", newline="\n")


def save_ru_configs():
    print(f"\n[FETCH] {RU_CIDR_SOURCE}")

    text = fetch_url(RU_CIDR_SOURCE)

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]

    ts = datetime.now(timezone.utc).strftime(
        "%Y-%m-%d %H:%M UTC"
    )

    header = (
        "# RU CIDR Configs | NosokVPNBot\n"
        f"# Обновлено: {ts}\n"
        f"# Строк: {len(lines)}\n"
        "# Telegram: https://t.me/"
        "NosokVPNBot?start=partner_8655864538\n"
        "#\n"
    )

    with open(
        "ru_configs.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(header)
        file.write("\n".join(lines))
        file.write("\n")

    print(
        f"[SAVE] ru_configs.txt — {len(lines)} строк"
    )

    return len(lines)


def update_readme(
    all_count,
    ver_count,
    ru_count,
    ts,
):
    try:
        with open(
            "README.md",
            "r",
            encoding="utf-8",
        ) as file:
            readme = file.read()

        ts_badge = (
            ts
            .replace("-", "_")
            .replace(" ", "_")
            .replace(":", "%3A")
        )

        stats_block = (
            "<!-- STATS_START -->\n"
            '<a href="https://raw.githubusercontent.com/'
            'aviamastersgh/vpn-free-russia/main/'
            'all_configs.txt">'
            f'<img src="https://img.shields.io/badge/'
            f'Все_конфиги-{all_count}-4C8BF5?'
            'style=for-the-badge&logo=server'
            '&logoColor=white" alt="All configs"/></a>\n'

            '<a href="https://raw.githubusercontent.com/'
            'aviamastersgh/vpn-free-russia/main/'
            'verified_configs.txt">'
            f'<img src="https://img.shields.io/badge/'
            f'Проверенные-{ver_count}-2ea44f?'
            'style=for-the-badge&logo=checkmarx'
            '&logoColor=white" alt="Verified configs"/></a>\n'

            '<a href="https://raw.githubusercontent.com/'
            'aviamastersgh/vpn-free-russia/main/'
            'ru_configs.txt">'
            f'<img src="https://img.shields.io/badge/'
            f'RU_обход-{ru_count}-2ea44f?'
            'style=for-the-badge&logo=checkmarx'
            '&logoColor=white" alt="RU configs"/></a>\n'

            f'<img src="https://img.shields.io/badge/'
            f'Обновлено-{ts_badge}-f97316?'
            'style=for-the-badge&logo=clockify'
            '&logoColor=white" alt="Updated"/>\n'

            "<!-- STATS_END -->"
        )

        updated = re.sub(
            r"<!-- STATS_START -->.*?<!-- STATS_END -->",
            stats_block,
            readme,
            flags=re.DOTALL,
        )

        if updated == readme:
            # Первый запуск после ручного обновления README:
            # пользовательский README мог ещё не содержать маркеры.
            #
            # В таком случае оборачиваем именно блок с тремя
            # config-badges, не затрагивая остальной SEO-текст.
            badge_pattern = re.compile(
                r'(?P<indent> *)<a href="https://raw\.githubusercontent\.com/'
                r'aviamastersgh/vpn-free-russia/main/'
                r'verified_configs\.txt">.*?</a>\\n'
                r'(?P<second>.*?all_configs\.txt">.*?</a>\\n'
                r'(?P<third>.*?ru_configs\.txt">.*?</a>)',
                re.DOTALL,
            )

            # Работаем непосредственно с markdown-текстом.
            block = re.search(
                r'(<a href="https://raw\.githubusercontent\.com/'
                r'aviamastersgh/vpn-free-russia/main/'
                r'verified_configs\.txt">.*?</a>\s*'
                r'<a href="https://raw\.githubusercontent\.com/'
                r'aviamastersgh/vpn-free-russia/main/'
                r'all_configs\.txt">.*?</a>\s*'
                r'<a href="https://raw\.githubusercontent\.com/'
                r'aviamastersgh/vpn-free-russia/main/'
                r'ru_configs\.txt">.*?</a>)',
                readme,
                flags=re.DOTALL,
            )

            if block:
                readme = readme[:block.start()] + (
                    "<!-- STATS_START -->\n"
                    + block.group(1)
                    + "\n<!-- STATS_END -->"
                ) + readme[block.end():]

                updated = re.sub(
                    r"<!-- STATS_START -->.*?<!-- STATS_END -->",
                    stats_block,
                    readme,
                    flags=re.DOTALL,
                )

            else:
                print(
                    "[WARN] Не удалось найти блок статистики README"
                )
                return

        with open(
            "README.md",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(updated)

        print("[UPDATE] README.md обновлён")

    except FileNotFoundError:
        print("[SKIP] README.md не найден")


def main():
    print("=" * 60)
    print(
        "VPN Fetcher:",
        datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M UTC"
        ),
    )
    print("=" * 60)

    all_configs = []
    seen = set()

    for url in SOURCES:
        print(f"[FETCH] {url[:90]}...")

        text = fetch_url(url)
        found = extract_configs(text)

        new = 0

        for config in found:
            if config not in seen:
                seen.add(config)
                all_configs.append(config)
                new += 1

        print(
            f"  → найдено {len(found)}, новых {new}"
        )

    print(
        f"\nВсего уникальных: {len(all_configs)}"
    )

    ts = datetime.now(timezone.utc).strftime(
        "%Y-%m-%d %H:%M UTC"
    )

    header_all = (
        "# Free VPN Configs | NosokVPNBot\n"
        f"# Обновлено: {ts}\n"
        f"# Всего: {len(all_configs)}\n"
        "# https://t.me/NosokVPNBot?"
        "start=partner_8655864538\n"
        "#\n"
    )

    # Дополнительная очистка перед публикацией.
    all_configs = [
        config.replace("\x00", "").strip()
        for config in all_configs
        if config and "\x00" not in config
    ]

    with open(
        "all_configs.txt",
        "w",
        encoding="utf-8",
        newline="\n",
    ) as file:
        file.write(
            "# Free VPN Configs | NosokVPNBot\n"
            f"# Обновлено: {ts}\n"
            f"# Всего: {len(all_configs)}\n"
            "# https://t.me/NosokVPNBot?"
            "start=partner_8655864538\n"
            "#\n"
        )
        file.write("\n".join(all_configs))
        file.write("\n")

    print(
        f"[SAVE] all_configs.txt — {len(all_configs)}"
    )

    print(
        f"\n[CHECK] TCP-проверка "
        f"({MAX_WORKERS} потоков)..."
    )

    sample = all_configs[:]
    random.shuffle(sample)

    verified = []
    checked = 0

    with ThreadPoolExecutor(
        max_workers=MAX_WORKERS
    ) as executor:

        futures = {
            executor.submit(check_config, config): config
            for config in sample
        }

        for future in as_completed(futures):
            checked += 1

            try:
                ok = future.result()
            except Exception:
                ok = False

            if ok:
                verified.append(
                    futures[future]
                )

                if len(verified) >= MAX_CONFIGS:
                    for item in futures:
                        item.cancel()
                    break

            if checked % 50 == 0:
                print(
                    f"  проверено {checked}/{len(sample)}, "
                    f"рабочих: {len(verified)}"
                )

    print(
        f"\nРабочих: {len(verified)} "
        f"из {checked}"
    )

    header_ver = (
        "# Verified VPN Configs | NosokVPNBot\n"
        f"# Обновлено: {ts}\n"
        f"# Проверенных: {len(verified)}\n"
        "# https://t.me/NosokVPNBot?"
        "start=partner_8655864538\n"
        "#\n"
    )

    with open(
        "verified_configs.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(header_ver)
        file.write("\n".join(verified))
        file.write("\n")

    print(
        f"[SAVE] verified_configs.txt — "
        f"{len(verified)}"
    )

    ru_count = save_ru_configs()

    update_readme(
        len(all_configs),
        len(verified),
        ru_count,
        ts,
    )

    print("\n✅ Готово!")


if __name__ == "__main__":
    main()
