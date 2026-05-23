# jobapp-py v0.3 - Python 3.13

FastAPI version of the Java Spring Boot MVC `JobApp` project, updated for local development with `python3.13`.

This version keeps the same learning structure:

| Java Spring Boot | Python FastAPI |
|---|---|
| `JobController` | `app/routers/jobs.py` |
| `JobService` | `app/services/job_service.py` |
| `JobRepo` | `app/repositories/*_job_repo.py` |
| `JobPost` model | `app/models.py` |
| JSP views | Swagger UI / REST JSON responses |

## v0.3 Python 3.13 + flat-file storage

The repository layer is now pluggable:

```text
Job API / Router
      ↓
Job Service
      ↓
JobRepository interface
      ↓
JsonJobRepo OR CsvJobRepo
```

This means the API and service layers should not need major changes when the backend later becomes PostgreSQL.

Supported now:

```text
json  -> app/data/jobs.json
csv   -> app/data/jobs.csv
```

Planned later:

```text
postgres -> SQLAlchemy + Alembic
```

## Does JSON map to Python dictionaries?

Yes.

```text
JSON object  -> Python dict
JSON array   -> Python list
JSON string  -> Python str
JSON number  -> Python int/float
JSON boolean -> Python bool
```

In this app, FastAPI/Pydantic converts request JSON into Python model objects, and the JSON repository saves those objects as a list of dictionaries.


## Python 3.13 notes

This package assumes your Pop!_OS machine has Python 3.13 and the matching venv support installed.

```bash
python3.13 --version
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The Dockerfile also uses:

```text
python:3.13-slim
```

## Run locally

```bash
cd jobapp-py-v0.3-python313
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Choose JSON storage

```bash
export JOBAPP_STORAGE_BACKEND=json
uvicorn app.main:app --reload
```

or:

```bash
./scripts/run-json.sh
```

## Choose CSV storage

```bash
export JOBAPP_STORAGE_BACKEND=csv
uvicorn app.main:app --reload
```

or:

```bash
./scripts/run-csv.sh
```

The CSV file can be opened with Excel or LibreOffice Calc. The `post_tech_stack` column stores multiple values like this:

```text
Python|FastAPI|PostgreSQL
```

## Useful endpoints

```text
GET    /health
GET    /version
GET    /storage
GET    /jobs
GET    /jobs/{post_id}
POST   /jobs
PUT    /jobs/{post_id}
DELETE /jobs/{post_id}
```

## Example create job

```bash
curl -X POST http://127.0.0.1:8000/jobs \
  -H 'Content-Type: application/json' \
  -d '{
    "post_profile": "Python API Developer",
    "post_desc": "Build REST APIs with FastAPI",
    "req_experience": 1,
    "post_tech_stack": ["Python", "FastAPI", "Docker"]
  }'
```

## Run tests

```bash
pytest
```

## Docker build/run

```bash
docker build -t jobapp-py:0.2.0 .
docker run --rm -p 8000:8000 -e JOBAPP_STORAGE_BACKEND=json jobapp-py:0.2.0
```

## Storage roadmap

```text
v0.1.0  FastAPI + JSON-file repository
v0.2.0  JSON or CSV repository selected by config
v0.3.0  Add search/filter endpoints
v0.4.0  Add SQLite repository
v0.5.0  Move to PostgreSQL + SQLAlchemy + Alembic
v0.6.0  Add Docker Compose
v0.7.0  Add Kubernetes manifests
v0.8.0  Add Prometheus metrics
v0.9.0  Add OAuth2/JWT auth
```

## Cassandra note

Cassandra is usually not the first database for this JobApp. PostgreSQL is better for learning CRUD, joins, transactions, relational data, and typical business apps. Cassandra makes sense later only for very high-volume, distributed, append-heavy access patterns, such as event logs, telemetry, time-series-like writes, or large-scale activity feeds.

---

# Platform Repository Notes

This app is the first reference implementation inside:

```text
motorweb
```

For full setup instructions, see the repository root:

```text
README.md
docs/setup/
docs/environments/
docs/diagrams/
```

This app should remain the validated working baseline while platform documentation, diagrams, GitHub setup, Linux users, and deployment workflows evolve around it.

---

# v0.5 Data Load / File-Backed Database

This app now separates source dataload files from active database files.

```text
data/dataload/input/dataload-jobs.csv       # source job tracker CSV
data/dataload/processed/dataload-jobs.json  # generated JSON
data/database-files/jobs/jobs.json          # active JSON database
data/database-files/jobs/jobs.csv           # active CSV database
data/schemas/jobs.schema.json               # schema reference
```

Run dataload:

```bash
source .venv/bin/activate
scripts/dataload/run-initial-dataload.sh
```

Run app using JSON database:

```bash
scripts/run-json.sh
```

Query examples:

```bash
curl http://127.0.0.1:8000/jobs
curl 'http://127.0.0.1:8000/jobs?status=Applied'
curl 'http://127.0.0.1:8000/jobs?keyword=Analyst'
curl 'http://127.0.0.1:8000/jobs?location=New%20York'
```
