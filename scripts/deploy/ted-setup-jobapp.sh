#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
APP_DIR="${REPO_ROOT}/apps/job-application-platform"

echo "[INFO] Repo root: $REPO_ROOT"
echo "[INFO] App dir: $APP_DIR"

if [[ ! -d "$APP_DIR" ]]; then
  echo "[ERROR] App directory not found: $APP_DIR"
  exit 1
fi

cd "$APP_DIR"

echo "[INFO] Creating Python 3.13 virtual environment..."
python3.13 -m venv .venv

echo "[INFO] Activating venv and installing requirements..."
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "[INFO] Running initial dataload..."
if [[ -x "scripts/dataload/run-initial-dataload.sh" ]]; then
  scripts/dataload/run-initial-dataload.sh
else
  echo "[ERROR] Missing executable dataload script: scripts/dataload/run-initial-dataload.sh"
  exit 1
fi

echo "[INFO] Setup complete."
