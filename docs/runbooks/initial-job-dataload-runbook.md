# Runbook - Initial Job Data Load

Use this to load job tracker data into the file-backed database.

## 1. Go to app folder

```bash
cd /opt/projects/motorweb/apps/job-application-platform
```

## 2. Activate venv

```bash
source .venv/bin/activate
```

## 3. Run initial dataload

```bash
scripts/dataload/run-initial-dataload.sh
```

This performs:

```text
CSV input → processed JSON → active JSON/CSV database files → validation
```

## 4. Run API in JSON mode

```bash
scripts/run-json.sh
```

## 5. Test GET endpoints

```bash
curl http://127.0.0.1:8000/storage
curl http://127.0.0.1:8000/jobs
curl 'http://127.0.0.1:8000/jobs?status=Applied'
curl 'http://127.0.0.1:8000/jobs?keyword=Analyst'
curl 'http://127.0.0.1:8000/jobs?location=New%20York'
```

## 6. Confirm active file

```bash
cat data/database-files/jobs/jobs.json | head
```
