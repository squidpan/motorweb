# Schema Evolution and Payload Design

This document explains how to change the Job Application Platform CSV table structure and JSON payload structure systematically.

The current seed file name is:

```text
apps/job-application-platform/data/dataload/input/dataload-jobs.csv
```

Do not use `.txt` for structured CSV input. Use `.csv` so Excel, Python, pandas, and future database tooling recognize the file correctly.

---

## Core principle

The CSV columns, JSON payload fields, API schemas, and future database table columns should evolve together.

Think of the data model as four connected layers:

```text
CSV dataload file
  ↓
JSON dataload / file-backed database
  ↓
REST API request/response payload
  ↓
future PostgreSQL table schema
```

When one layer changes, review the others.

---

## Current v1 fields

```text
job_position
company
max_salary
location
status
date_saved
```

The generated JSON adds:

```text
id
```

Example:

```json
{
  "id": 1,
  "job_position": "Product Support Analyst",
  "company": "Liquidnet, Inc.",
  "max_salary": 105000,
  "location": "New York",
  "status": "Bookmarked",
  "date_saved": "04/07/2026"
}
```

---

## Recommended change process

Use this process when you want to add, remove, or rename fields.

### Step 1 - Create a new CSV version

Do not overwrite the original immediately.

Create:

```text
apps/job-application-platform/data/dataload/input/versions/dataload-jobs-v2-example.csv
```

Example added fields:

```text
min_salary
currency
work_mode
date_applied
source_url
notes
```

---

### Step 2 - Create or update a JSON schema

Schema files live under:

```text
apps/job-application-platform/data/schemas/
```

Current examples:

```text
jobs.schema.v1.json
jobs.schema.v2-example.json
```

---

### Step 3 - Update the converter mapping

The CSV-to-JSON converter should have a clear mapping from CSV column names to JSON field names.

Simple case:

```text
CSV header name = JSON field name
```

More complex case:

```text
max_salary text "$105,000" → integer 105000
blank date_applied → null
blank location → ""
```

---

### Step 4 - Update API model/schema

If the API accepts or returns the new fields, update the API model.

For FastAPI/Pydantic this usually means updating the job schema/model.

Future database version means updating:

```text
SQLAlchemy model
Alembic migration
PostgreSQL DDL
```

---

### Step 5 - Keep backward compatibility if useful

Do not break old dataload files immediately.

Prefer:

```text
v1 converter supports old CSV
v2 converter supports new CSV
```

or one flexible converter that handles missing optional fields.

---

### Step 6 - Regenerate JSON

After changing CSV structure:

```bash
cd /opt/projects/motorweb/apps/job-application-platform
python scripts/dataload/csv_to_json.py \
  --input data/dataload/input/dataload-jobs.csv \
  --output data/dataload/processed/dataload-jobs.json
```

Then load or copy the generated JSON into the file-backed database area.

---

## Field change guidelines

### Adding a field

Safe if optional.

Example:

```text
work_mode
```

Add it to:

```text
CSV header
JSON schema
API model if exposed
database schema later
tests/docs
```

---

### Renaming a field

More risky.

Example:

```text
job_position → title
```

Prefer to avoid renames unless needed.

If renamed, document:

```text
old field
new field
migration rule
affected files
```

---

### Removing a field

Most risky.

Confirm no API, test, query, or future DB logic depends on it.

---

### Changing a type

Example:

```text
max_salary string → integer
```

Document conversion rules clearly.

Recommended normalized type:

```text
max_salary: integer
```

---

## Future PostgreSQL mapping

Current v1 table concept:

```sql
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY,
    job_position TEXT NOT NULL,
    company TEXT NOT NULL,
    max_salary INTEGER,
    location TEXT,
    status TEXT NOT NULL,
    date_saved DATE
);
```

For future versions, add migrations instead of manually changing tables.

Example future fields:

```sql
ALTER TABLE jobs ADD COLUMN min_salary INTEGER;
ALTER TABLE jobs ADD COLUMN currency TEXT DEFAULT 'USD';
ALTER TABLE jobs ADD COLUMN work_mode TEXT;
ALTER TABLE jobs ADD COLUMN date_applied DATE;
ALTER TABLE jobs ADD COLUMN source_url TEXT;
ALTER TABLE jobs ADD COLUMN notes TEXT;
```

---

## Recommended naming convention

Use:

```text
snake_case
```

Good:

```text
job_position
max_salary
date_saved
date_applied
source_url
```

Avoid:

```text
Job Position
Max Salary
date saved
```

because spaces and mixed case create unnecessary mapping issues.

---

## Design recommendation

For `motorweb`, treat the dataload CSV as the first version of your data contract.

Then evolve toward:

```text
CSV contract
JSON contract
OpenAPI contract
PostgreSQL schema
```

in a controlled way.
