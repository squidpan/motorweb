# File-Backed Database Design

The current `motorweb` Job Application Platform uses files as a temporary database before PostgreSQL is introduced.

## Goals

```text
CSV input from job tracker / Excel
JSON generated for Python scripts and API loading
JSON or CSV active database files
Repository layer hides storage backend
Future PostgreSQL schema can be derived from the same fields
```

## Data lifecycle

```text
source CSV/text export
  ↓
data/dataload/input/dataload-jobs.csv
  ↓ csv_to_jobs_json.py
data/dataload/processed/dataload-jobs.json
  ↓ load_jobs_database_files.py
data/database-files/jobs/jobs.json
  ↓ JsonJobRepo
GET /jobs
POST /jobs
PUT /jobs/{id}
DELETE /jobs/{id}
```

## Active fields

```text
post_id
job_position
company
max_salary
location
status
date_saved
source
notes
```

## PostgreSQL mapping later

A future `jobs` table can start from this shape:

```sql
CREATE TABLE jobs (
  post_id INTEGER PRIMARY KEY,
  job_position TEXT NOT NULL,
  company TEXT NOT NULL,
  max_salary INTEGER DEFAULT 0,
  location TEXT DEFAULT '',
  status TEXT DEFAULT 'Bookmarked',
  date_saved DATE,
  source TEXT DEFAULT 'manual',
  notes TEXT DEFAULT ''
);
```

The flat-file version currently keeps `date_saved` as `MM/DD/YYYY` text. PostgreSQL should convert it to a real `DATE` field.
