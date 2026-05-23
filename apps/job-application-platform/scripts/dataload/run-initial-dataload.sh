#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

python scripts/dataload/csv_to_jobs_json.py   --input data/dataload/input/dataload-jobs.csv   --output data/dataload/processed/dataload-jobs.json   --source teal

python scripts/dataload/validate_jobs_json.py   --input-json data/dataload/processed/dataload-jobs.json

python scripts/dataload/load_jobs_database_files.py   --input-json data/dataload/processed/dataload-jobs.json

python scripts/dataload/validate_jobs_json.py   --input-json data/database-files/jobs/jobs.json

echo "Initial dataload complete. Run: JOBAPP_STORAGE_BACKEND=json uvicorn app.main:app --reload"
