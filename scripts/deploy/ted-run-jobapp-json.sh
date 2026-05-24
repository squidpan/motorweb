#!/usr/bin/env bash
set -euo pipefail

PORT="${1:-8000}"

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
APP_DIR="${REPO_ROOT}/apps/job-application-platform"

cd "$APP_DIR"

if [[ ! -d ".venv" ]]; then
  echo "[ERROR] .venv not found. Run scripts/deploy/ted-setup-jobapp.sh first."
  exit 1
fi

source .venv/bin/activate
export JOBAPP_STORAGE_BACKEND=json

echo "[INFO] Starting Job Application Platform"
echo "[INFO] Backend: $JOBAPP_STORAGE_BACKEND"
echo "[INFO] URL: http://127.0.0.1:${PORT}/docs"

uvicorn app.main:app --reload --port "$PORT"
