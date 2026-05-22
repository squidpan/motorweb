#!/usr/bin/env bash
set -euo pipefail

export JOBAPP_STORAGE_BACKEND=csv
uvicorn app.main:app --reload
