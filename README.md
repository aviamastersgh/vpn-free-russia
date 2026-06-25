<!-- SEO meta-description (GitHub reads первые ~160 символов) -->
<!-- Free VPN configs for Russia 2024-2026. VLESS, VMess, Shadowsocks, Trojan, Hysteria2. Auto-updated every 6 hours. Works with Happ, Incy, v2rayNG, Streisand, NekoBox. Bypass RKN censorship. -->

<div align="center">

# 🚀 Free VPN Configs — Бесплатный VPN для России

**Публичные, бесплатные VPN-конфигурации. Обновляются каждые 6 часов автоматически.**  
VLESS · VMess · Shadowsocks · Trojan · Hysteria2

[![Configs](https://img.shields.io/badge/Все_конфиги-<!--STATS_ALL-->716<!--/STATS_ALL-->-blue?style=for-the-badge)](https://raw.githubusercontent.com/happ-incy-bot/vpn-free-russia/main/all_configs.txt)
[![Verified](https://img.shields.io/badge/Проверенные-<!--STATS_VER-->447<!--/STATS_VER-->-brightgreen?style=for-the-badge)](https://raw.githubusercontent.com/happ-incy-bot/vpn-free-russia/main/verified_configs.txt)
[![Updated](https://img.shields.io/badge/Обновлено-<!--STATS_TS-->2026-06-25 14:27 UTC<!--/STATS_TS-->-orange?style=for-the-badge)](#)
[![Telegram](https://img.shields.io/badge/Telegram_бот-@happ__incy__bot-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/happ_incy_bot)

</div>

---

## 📖 Введение

Этот репозиторий — **агрегатор публичных бесплатных VPN-конфигураций**, работающих на территории России для обхода блокировок Роскомнадзора (РКН).

Каждые **6 часов** скрипт собирает конфиги из десятков открытых источников, проверяет TCP-доступность каждого сервера и публикует два файла:

- **`all_configs.txt`** — все найденные конфиги (без проверки)  
- **`verified_configs.txt`** — только те, чей сервер откликнулся на момент проверки

> ⚠️ Конфиги **публичные и общедоступные** — серверы бесплатны для всех. Никакой подписки не нужно: просто добавьте ссылку в клиент.

---

## ⚡ Быстрое подключение — одна кнопка

> Нажмите ссылку прямо с телефона — приложение откроется автоматически и предложит добавить список серверов.

### 📱 Happ

| Список | Ссылка для Happ |
|--------|----------------|
| ✅ Проверенные (рекомендуется) | [Открыть в Happ](happ://add/https://raw.githubusercontent.com/happ-incy-bot/vpn-free-russia/main/verified_configs.txt) |
| 📋 Все конфиги | [Открыть в Happ](happ://add/https://raw.githubusercontent.com/happ-incy-bot/vpn-free-russia/main/all_configs.txt) |

### 🐛 Incy

| Список | Ссылка для Incy |
|--------|----------------|
| ✅ Проверенные (рекомендуется) | [Открыть в Incy](incy://import/https://raw.githubusercontent.com/happ-incy-bot/vpn-free-russia/main/verified_configs.txt) |
| 📋 Все конфиги | [Открыть в Incy](incy://import/https://raw.githubusercontent.com/happ-incy-bot/vpn-free-russia/main/all_configs.txt) |

> **Как это работает?** Ссылка открывает приложение и импортирует список серверов напрямую в клиент — никаких подписок, никакой регистрации. Серверы публичные и доступны всем бесплатно.

---

## 📱 Поддерживаемые клиенты

| Клиент | Платформа | Как добавить |
|--------|-----------|--------------|
| **Happ** | Android / iOS | [happ://add/{{ССЫЛКА}}](#-happ) |
| **Incy** | Android / iOS | [incy://import/{{ССЫЛКА}}](#-incy) |
| v2rayNG | Android | Импорт → из буфера обмена / URL |
| Streisand | iOS | Добавить подписку |
| NekoBox | Android | Профили → добавить |
| v2rayN | Windows | Подписка → добавить |
| Hiddify | Android / Desktop | Добавить профиль |
| Karing | Android / iOS / Desktop | Импорт ссылки |

---

## 🔒 Стабильный VPN

Публичные конфиги могут иногда прерываться — это нормально для бесплатных серверов.  
Для **надёжного и стабильного** соединения воспользуйтесь нашим Telegram-ботом:

<div align="center">

### 🤖 [@happ_incy_bot](https://t.me/happ_incy_bot)

**Стабильный VPN · Личный ключ · Быстрое подключение**

</div>

---

## 📂 Файлы репозитория

| Файл | Описание | Ссылка |
|------|----------|--------|
| `all_configs.txt` | Все конфиги из всех источников | [Raw](https://raw.githubusercontent.com/happ-incy-bot/vpn-free-russia/main/all_configs.txt) · [GitHack](https://raw.githack.com/happ-incy-bot/vpn-free-russia/main/all_configs.txt) |
| `verified_configs.txt` | Только рабочие (проверены TCP) | [Raw](https://raw.githubusercontent.com/happ-incy-bot/vpn-free-russia/main/verified_configs.txt) · [GitHack](https://raw.githack.com/happ-incy-bot/vpn-free-russia/main/verified_configs.txt) |

> **GitHack** работает как прокси — используйте его если GitHub Raw заблокирован.

---

## 🔄 Как устроено обновление

```
Каждые 6 часов на VPS:
  1. Скрипт скачивает конфиги из ~15 публичных источников
  2. Убирает дубликаты
  3. Проверяет каждый конфиг: TCP-соединение до host:port
  4. Сохраняет два файла и делает git commit + push
```

---

## 🛠 Протоколы

- **VLESS** (в т.ч. Reality, XTLS) — наиболее устойчив к блокировкам РКН
- **VMess** — классика, широко поддерживается
- **Shadowsocks** — быстрый, лёгкий
- **Trojan** — маскируется под HTTPS
- **Hysteria2** — UDP, высокая скорость
- **TUIC** — современный, на QUIC

---

## 🌍 Если GitHub заблокирован

Используйте зеркала для доступа к файлам без VPN:

| Зеркало | Ссылка (verified) |
|---------|-------------------|
| GitHack | `https://raw.githack.com/happ-incy-bot/vpn-free-russia/main/verified_configs.txt` |
| jsDelivr | `https://cdn.jsdelivr.net/gh/happ-incy-bot/vpn-free-russia@main/verified_configs.txt` |
| Yandex Translate | `https://translate.yandex.ru/translate?url=https://raw.githubusercontent.com/happ-incy-bot/vpn-free-russia/main/verified_configs.txt&lang=ru-en` |

---

## 📋 Источники

Конфиги собираются из следующих публичных репозиториев:

| # | Репозиторий | Протоколы |
|---|-------------|-----------|
| 1 | [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia) | VLESS, Reality |
| 2 | [barry-far/V2ray-Configs](https://github.com/barry-far/V2ray-Configs) | VLESS, VMess, SS, Trojan |
| 3 | [mahdibland/V2RayAggregator](https://github.com/mahdibland/V2RayAggregator) | Mix |
| 4 | [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers) | Mix |
| 5 | [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls) | Mix |
| 6 | [freefq/free](https://github.com/freefq/free) | VMess |
| 7 | [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe) | Mix |
| 8 | [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree) | VMess |

Все источники — публичные репозитории с открытыми лицензиями.  
Мы не генерируем и не продаём серверы — только агрегируем и проверяем.

---

## ⭐ Поддержи проект

Если помогло — поставь звезду ⭐ и поделись с теми, кому нужен VPN.

[![Telegram](https://img.shields.io/badge/@happ__incy__bot-Telegram-2CA5E0?style=flat&logo=telegram)](https://t.me/happ_incy_bot)

---

<!-- SEO keywords (hidden) -->
<!--
vpn россия бесплатно, vpn для России 2025 2026, обход блокировок РКН, vless бесплатно,
free vless configs, free vpn configs russia, vpn keys free, vless reality free,
vmess free, shadowsocks free russia, trojan vpn free, hysteria2 free,
happ vpn, incy vpn, v2rayng configs, streisand vpn, nekobox configs,
vpn ключи бесплатно, впн ключи, впн для андроид, впн для айфон,
обход роскомнадзора, ркн обход, белые списки обход, vpn config subscription,
free vpn subscription, vpn без регистрации, vpn бесплатно без ограничений
-->
