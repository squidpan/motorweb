#!/usr/bin/env bash
set -euo pipefail
export JOBAPP_STORAGE_BACKEND=json
export JOBAPP_JSON_DATA_FILE=data/database-files/jobs/jobs.json
uvicorn app.main:app --reload
