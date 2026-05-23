# Runbook - Modify Job Dataload Schema

Use this runbook when changing the job CSV columns or JSON payload structure.

---

## 1. Start from a clean branch

```bash
cd /opt/projects/motorweb
git switch main
git pull
git switch -c feature/job-schema-v2
```

---

## 2. Copy the current CSV as a new version

```bash
cd apps/job-application-platform
cp data/dataload/input/dataload-jobs.csv \
   data/dataload/input/versions/dataload-jobs-v2.csv
```

Edit the v2 file.

---

## 3. Decide the field changes

Document changes in a small table.

Example:

| Change | Field | Notes |
|---|---|---|
| Add | `min_salary` | optional integer |
| Add | `currency` | default `USD` |
| Add | `work_mode` | Remote/Hybrid/Onsite/Unknown |
| Add | `date_applied` | optional date |
| Add | `source_url` | optional |
| Add | `notes` | optional |

---

## 4. Update JSON schema

Create:

```text
data/schemas/jobs.schema.v2.json
```

Use:

```text
data/schemas/jobs.schema.v2-example.json
```

as the starting point.

---

## 5. Convert CSV to JSON

```bash
python scripts/dataload/csv_to_json.py \
  --input data/dataload/input/versions/dataload-jobs-v2.csv \
  --output data/dataload/processed/dataload-jobs-v2.json
```

---

## 6. Inspect JSON

```bash
python -m json.tool data/dataload/processed/dataload-jobs-v2.json | head -80
```

---

## 7. Load into file-backed database

For testing, copy it into the database files area:

```bash
cp data/dataload/processed/dataload-jobs-v2.json \
   data/database-files/jobs/jobs.json
```

If needed, also update CSV database copy:

```bash
cp data/dataload/input/versions/dataload-jobs-v2.csv \
   data/database-files/jobs/jobs.csv
```

---

## 8. Run the app

```bash
source .venv/bin/activate
scripts/run-json.sh
```

---

## 9. Test GET endpoints

```bash
curl http://127.0.0.1:8000/jobs
curl 'http://127.0.0.1:8000/jobs?status=Applied'
curl 'http://127.0.0.1:8000/jobs?keyword=Analyst'
```

---

## 10. Update API model if needed

If new fields should appear in REST responses or be accepted in POST/PUT, update the FastAPI/Pydantic model.

---

## 11. Future PostgreSQL step

When PostgreSQL is added, create a migration instead of manually changing tables.

Future pattern:

```bash
alembic revision -m "add job schema v2 fields"
alembic upgrade head
```

---

## 12. Commit

```bash
git status
git add .
git commit -m "Add job dataload schema v2"
git push -u origin feature/job-schema-v2
```
