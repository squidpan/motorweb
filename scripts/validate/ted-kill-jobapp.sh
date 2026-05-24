#!/usr/bin/env bash
set -euo pipefail

PORT="${1:-8000}"

echo "[INFO] Looking for processes listening on port ${PORT}..."
sudo lsof -nP -iTCP:"$PORT" -sTCP:LISTEN || true

echo "[INFO] Attempting to kill uvicorn processes..."
pkill -f uvicorn || true

echo "[INFO] Checking port again..."
if ss -tulpen | grep -q ":${PORT}"; then
  echo "[WARNING] Port ${PORT} still appears in use."
  echo "Try:"
  echo "  sudo fuser -k ${PORT}/tcp"
else
  echo "[INFO] Port ${PORT} appears free."
fi
