#!/usr/bin/env python3
"""
VPN Config Fetcher & Validator
Парсит VLESS/VMess/SS/Trojan/Hysteria2 конфиги из публичных источников,
проверяет их и сохраняет в all_configs.txt и verified_configs.txt
"""

import re
import sys
import time
import random
import socket
import base64
import urllib.request
import urllib.error
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

# ─── НАСТРОЙКИ ────────────────────────────────────────────────────────────────
TIMEOUT = 8           # секунды на проверку одного конфига
MAX_WORKERS = 30      # параллельных потоков при проверке
MAX_CONFIGS = 500     # лимит конфигов в verified_configs.txt

# ─── ИСТОЧНИКИ ────────────────────────────────────────────────────────────────
SOURCES = [
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Vless-Reality-White-Lists-Rus-Mobile.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Vless-Reality-White-Lists-Rus-Mobile-2.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Splitted-By-Protocol/vmess.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Splitted-By-Protocol/trojan.txt",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity.txt",
    "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub",
    "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt",
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt",
    "https://raw.githubusercontent.com/rvptr/vpn/main/configs",
    "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
]

VALID_PREFIXES = (
    "vless://", "vmess://", "ss://", "trojan://",
    "hysteria2://", "hy2://", "tuic://", "wireguard://",
)

def fetch_url(url: str) -> str:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (VPN-Bot/1.0)"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
        try:
            decoded = base64.b64decode(raw + b"==").decode("utf-8", errors="ignore")
            if any(p in decoded for p in VALID_PREFIXES):
                return decoded
        except Exception:
            pass
        return raw.decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"  [SKIP] {url[:70]}... → {e}", file=sys.stderr)
        return ""

def extract_configs(text: str) -> list:
    configs = []
    for line in text.splitlines():
        line = line.strip()
        if any(line.startswith(p) for p in VALID_PREFIXES):
            configs.append(line)
    return configs

def parse_host_port(config: str):
    try:
        if config.startswith("vmess://"):
            payload = config[8:]
            padding = "=" * (4 - len(payload) % 4)
            data = base64.b64decode(payload + padding).decode("utf-8", errors="ignore")
            import json
            obj = json.loads(data)
            return obj.get("add"), int(obj.get("port", 443))

        m = re.match(r"[a-z0-9]+://[^@]+@([^:/?#]+):(\d+)", config)
        if m:
            return m.group(1), int(m.group(2))

        if config.startswith("ss://"):
            body = config[5:].split("#")[0]
            if "@" in body:
                m = re.match(r"[^@]+@([^:]+):(\d+)", body)
                if m:
                    return m.group(1), int(m.group(2))
    except Exception:
        pass
    return None, None

def check_config(config: str) -> bool:
    host, port = parse_host_port(config)
    if not host or not port:
        return False
    try:
        with socket.create_connection((host, port), timeout=TIMEOUT):
            return True
    except Exception:
        return False

def main():
    print("=" * 60)
    print(f"VPN Fetcher запущен: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)

    all_configs = []
    seen = set()

    for url in SOURCES:
        print(f"[FETCH] {url[:70]}...")
        text = fetch_url(url)
        found = extract_configs(text)
        new = 0
        for c in found:
            if c not in seen:
                seen.add(c)
                all_configs.append(c)
                new += 1
        print(f"  → найдено {len(found)}, новых {new}")

    print(f"\nВсего уникальных конфигов: {len(all_configs)}")

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = (
        f"# 🌐 Free VPN Configs | happ_incy_bot\n"
        f"# Обновлено: {ts}\n"
        f"# Всего конфигов: {len(all_configs)}\n"
        f"# Подробнее: https://github.com/aviamastersgh/vpn-free-russia\n"
        f"# Telegram: https://t.me/happ_incy_bot\n"
        "#\n"
    )
    with open("all_configs.txt", "w", encoding="utf-8") as f:
        f.write(header)
        f.write("\n".join(all_configs))
        f.write("\n")
    print(f"[SAVE] all_configs.txt — {len(all_configs)} конфигов")

    print(f"\n[CHECK] Проверяем TCP-доступность ({MAX_WORKERS} потоков)...")
    sample = all_configs[:]
    random.shuffle(sample)

    verified = []
    checked = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(check_config, c): c for c in sample}
        for future in as_completed(futures):
            checked += 1
            config = futures[future]
            try:
                ok = future.result()
            except Exception:
                ok = False
            if ok:
                verified.append(config)
                if len(verified) >= MAX_CONFIGS:
                    for f in futures:
                        f.cancel()
                    break
            if checked % 50 == 0:
                print(f"  проверено {checked}/{len(sample)}, рабочих: {len(verified)}")

    print(f"\nРабочих конфигов: {len(verified)} из {checked} проверено")

    v_header = (
        f"# ✅ Verified VPN Configs | happ_incy_bot\n"
        f"# Обновлено: {ts}\n"
        f"# Проверенных: {len(verified)}\n"
        f"# Проверка: TCP-соединение до хоста:порт\n"
        f"# Подробнее: https://github.com/aviamastersgh/vpn-free-russia\n"
        f"# Telegram: https://t.me/happ_incy_bot\n"
        "#\n"
    )
    with open("verified_configs.txt", "w", encoding="utf-8") as f:
        f.write(v_header)
        f.write("\n".join(verified))
        f.write("\n")
    print(f"[SAVE] verified_configs.txt — {len(verified)} конфигов")

    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme = f.read()
        readme = re.sub(
            r"(<!--STATS_ALL-->).*?(<!--/STATS_ALL-->)",
            f"<!--STATS_ALL-->{len(all_configs)}<!--/STATS_ALL-->",
            readme,
        )
        readme = re.sub(
            r"(<!--STATS_VER-->).*?(<!--/STATS_VER-->)",
            f"<!--STATS_VER-->{len(verified)}<!--/STATS_VER-->",
            readme,
        )
        readme = re.sub(
            r"(<!--STATS_TS-->).*?(<!--/STATS_TS-->)",
            f"<!--STATS_TS-->{ts}<!--/STATS_TS-->",
            readme,
        )
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme)
        print("[UPDATE] README.md обновлён")
    except FileNotFoundError:
        print("[SKIP] README.md не найден, пропускаем")

    print("\n✅ Готово!")


if __name__ == "__main__":
    main()
