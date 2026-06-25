#!/bin/bash
# =============================================================
# run_vpn_update.sh — обёртка для cron
# Запускать из корня репозитория:
#   bash scripts/run_vpn_update.sh
#
# Cron (каждые 6 часов):
#   0 */6 * * * cd /root/vpn-free-russia && bash scripts/run_vpn_update.sh >> /var/log/vpn_update.log 2>&1
# =============================================================
set -euo pipefail
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"
echo ""
echo "======================================================"
echo "  VPN Update — $(date -u '+%Y-%m-%d %H:%M UTC')"
echo "======================================================"
# ── 1. Настройка git ──────────────────────────────────────
git config user.email "bot@vpn-free-russia"
git config user.name  "vpn-bot"
# ── 2. Подтягиваем последние изменения ───────────────────
echo "[GIT] pull..."
git pull --rebase origin main || true
# ── 3. Запускаем парсер ───────────────────────────────────
echo "[PY] fetch + verify..."
python3 scripts/fetch_vpn.py
# ── 4. Коммитим если есть изменения ──────────────────────
if git diff --quiet all_configs.txt verified_configs.txt ru_configs.txt README.md 2>/dev/null; then
    echo "[GIT] Нет изменений, пропускаем коммит"
    exit 0
fi
TOTAL=$(grep -v '^#' all_configs.txt | grep -v '^$' | wc -l | tr -d ' ')
VERIFIED=$(grep -v '^#' verified_configs.txt | grep -v '^$' | wc -l | tr -d ' ')
TS=$(date -u '+%Y-%m-%d %H:%M UTC')
git add all_configs.txt verified_configs.txt ru_configs.txt README.md
git commit -m "🔄 auto-update: all=${TOTAL}, verified=${VERIFIED} [${TS}]"
echo "[GIT] push..."
git push origin main
echo "✅ Done!"
