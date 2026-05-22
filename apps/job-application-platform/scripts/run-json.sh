#!/usr/bin/env bash
set -euo pipefail

export JOBAPP_STORAGE_BACKEND=json
uvicorn app.main:app --reload
