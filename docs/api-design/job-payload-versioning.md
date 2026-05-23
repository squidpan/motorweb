# Job Payload Versioning

The Job Application Platform payload will evolve over time.

This document explains the versioning approach.

---

## Current payload version

Current practical version:

```text
jobs.v1
```

Fields:

```text
id
job_position
company
max_salary
location
status
date_saved
```

---

## Why version payloads?

Payloads change when the business model changes.

Examples:

```text
add date_applied
add work_mode
add source_url
rename job_position to title
split salary into min_salary and max_salary
```

Without version discipline, CSV files, JSON files, API models, and future database tables drift apart.

---

## Recommended version locations

CSV examples:

```text
data/dataload/input/dataload-jobs.csv
data/dataload/input/versions/dataload-jobs-v1.csv
data/dataload/input/versions/dataload-jobs-v2.csv
```

JSON schemas:

```text
data/schemas/jobs.schema.v1.json
data/schemas/jobs.schema.v2.json
```

Processed JSON:

```text
data/dataload/processed/dataload-jobs.json
data/dataload/processed/dataload-jobs-v2.json
```

---

## API versioning later

Eventually APIs can use:

```text
/api/v1/jobs
/api/v2/jobs
```

For now, keep one API and evolve carefully.

---

## Backward compatibility rule

When possible:

```text
new fields should be optional first
old CSV should still load
old JSON should still be readable
```

---

## Good field naming

Use snake_case:

```text
job_position
date_saved
date_applied
source_url
max_salary
```

Do not use spaces or mixed case in machine-readable payloads.

---

## Future database mapping

Each payload version should eventually map to:

```text
PostgreSQL table schema
migration script
test data
OpenAPI schema
```
