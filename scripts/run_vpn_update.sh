#!/bin/bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

echo ""
echo "======================================================"
echo "  VPN Update — $(date -u '+%Y-%m-%d %H:%M UTC')"
echo "======================================================"

git config user.email "bot@vpn-free-russia"
git config user.name  "vpn-bot"

echo "[GIT] Проверяем состояние..."
if ! git diff --quiet || [ -n "$(git status --porcelain --untracked-files=no)" ]; then
    echo "[GIT] Найдены локальные tracked-изменения."
    echo "[GIT] Останавливаемся, чтобы ничего не затереть."
    git status --short
    exit 1
fi

echo "[GIT] pull --rebase..."
git pull --rebase origin main

echo "[PY] fetch + verify..."
python3 scripts/fetch_vpn.py

if git diff --quiet all_configs.txt verified_configs.txt ru_configs.txt README.md 2>/dev/null; then
    echo "[GIT] Нет изменений, пропускаем коммит."
    exit 0
fi

TOTAL=$(python3 - <<'PYCOUNT'
from pathlib import Path
print(sum(
    1
    for line in Path("all_configs.txt").read_text(
        encoding="utf-8"
    ).splitlines()
    if line.strip() and not line.startswith("#")
))
PYCOUNT
)

VERIFIED=$(python3 - <<'PYCOUNT'
from pathlib import Path
print(sum(
    1
    for line in Path("verified_configs.txt").read_text(
        encoding="utf-8"
    ).splitlines()
    if line.strip() and not line.startswith("#")
))
PYCOUNT
)
TS=$(date -u '+%Y-%m-%d %H:%M UTC')

echo "[GIT] Изменения:"
git status --short

git add all_configs.txt verified_configs.txt ru_configs.txt README.md

git commit -m "🔄 auto-update: all=${TOTAL}, verified=${VERIFIED} [${TS}]"

echo "[GIT] push..."
git push origin main

echo "✅ Done!"
