#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${1:-http://127.0.0.1:8000}"

echo "[INFO] Validating Job Application Platform at: $BASE_URL"

echo
echo "[INFO] Health check"
curl -fsS "${BASE_URL}/health"
echo

echo
echo "[INFO] Storage backend"
curl -fsS "${BASE_URL}/storage"
echo

echo
echo "[INFO] Get all jobs"
curl -fsS "${BASE_URL}/jobs" | python -m json.tool | head -80
echo

echo
echo "[INFO] Query Applied jobs"
curl -fsS "${BASE_URL}/jobs?status=Applied" | python -m json.tool | head -80
echo

echo
echo "[INFO] Keyword query: Analyst"
curl -fsS "${BASE_URL}/jobs?keyword=Analyst" | python -m json.tool | head -80
echo

echo
echo "[INFO] Validation completed successfully."
