# motorweb v0.5.2 Full Dataload + Schema Evolution Package

This is a full overlay package that includes:

```text
motorweb-v0.5-dataload-foundation
+
motorweb-v0.5.1-dataload-schema-evolution
```

It includes:

```text
CSV dataload input
CSV-to-JSON conversion utility
processed JSON dataload output
file-backed JSON database area
file-backed CSV database area
job schema files
versioned dataload examples
schema evolution documentation
payload versioning documentation
runbooks for initial dataload and schema changes
```

Primary dataload source:

```text
apps/job-application-platform/data/dataload/input/dataload-jobs.csv
```

Primary generated JSON:

```text
apps/job-application-platform/data/dataload/processed/dataload-jobs.json
```

Primary file-backed database files:

```text
apps/job-application-platform/data/database-files/jobs/jobs.json
apps/job-application-platform/data/database-files/jobs/jobs.csv
```

Schema examples:

```text
apps/job-application-platform/data/schemas/jobs.schema.v1.json
apps/job-application-platform/data/schemas/jobs.schema.v2-example.json
```

Key docs:

```text
docs/data/file-backed-database-design.md
docs/data/schema-evolution-and-payload-design.md
docs/runbooks/initial-job-dataload-runbook.md
docs/runbooks/modify-job-dataload-schema-runbook.md
docs/api-design/jobs-query-api.md
docs/api-design/job-payload-versioning.md
```

Use this package as the baseline for the dataload/file-backed-database work.
