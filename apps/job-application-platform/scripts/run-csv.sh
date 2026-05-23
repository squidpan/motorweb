#!/usr/bin/env bash
set -euo pipefail
export JOBAPP_STORAGE_BACKEND=csv
export JOBAPP_CSV_DATA_FILE=data/database-files/jobs/jobs.csv
uvicorn app.main:app --reload
