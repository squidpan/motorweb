# README Update - v0.5.1 Dataload Schema Evolution Addendum

Add this near the dataload section of the root README.

---

## Flexible Dataload and Payload Evolution

The job dataload seed file is now standardized as:

```text
apps/job-application-platform/data/dataload/input/dataload-jobs.csv
```

Use `.csv`, not `.txt`, for structured table input.

The current payload fields are:

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

To modify the table structure or JSON payload cleanly, follow:

```text
docs/data/schema-evolution-and-payload-design.md
docs/runbooks/modify-job-dataload-schema-runbook.md
docs/api-design/job-payload-versioning.md
```

Versioned examples live in:

```text
apps/job-application-platform/data/dataload/input/versions/
apps/job-application-platform/data/schemas/
```

The design goal is that CSV, JSON, REST API payloads, and future PostgreSQL schemas evolve together instead of drifting apart.
