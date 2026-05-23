# Job Application Platform Data Folder

This folder separates initial dataload files from the active flat-file database.

```text
data/
├── dataload/
│   ├── input/          # source CSV/text exports, e.g. Teal job tracker export
│   └── processed/      # generated JSON ready to load
│
├── database-files/
│   ├── jobs/           # active file-backed database used by the API
│   │   ├── jobs.json
│   │   └── jobs.csv
│   └── archive/        # backup copies created before reloads
│
└── schemas/
    └── jobs.schema.json
```

Current app default:

```text
JSON database: data/database-files/jobs/jobs.json
CSV database:  data/database-files/jobs/jobs.csv
```

Use JSON for API/script loading and CSV for Excel/LibreOffice review.
