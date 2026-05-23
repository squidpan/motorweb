# motorweb Folder Structure

This document explains the high-level repository layout.

---

## Current Repository Tree

```text
motorweb/
├── README.md
├── apps/
│   └── job-application-platform/
│       ├── app/
│       │   ├── main.py
│       │   ├── routers/
│       │   ├── services/
│       │   ├── repositories/
│       │   └── models.py
│       │
│       ├── data/
│       │   ├── jobs.json
│       │   └── jobs.csv
│       │
│       ├── tests/
│       ├── scripts/
│       ├── Dockerfile
│       ├── README.md
│       ├── pyproject.toml
│       └── requirements.txt
│
├── docs/
│   ├── setup/
│   ├── requirements/
│   ├── user-stories/
│   ├── acceptance-criteria/
│   ├── api-design/
│   ├── testing/
│   ├── troubleshooting/
│   ├── runbooks/
│   ├── architecture/
│   ├── diagrams/
│   └── obsidian/
│
├── infra/
│   ├── docker/
│   ├── k8s/
│   └── monitoring/
│
└── scripts/
    ├── setup/
    ├── git/
    └── env/
```

---

## Conceptual Meaning

```text
apps/
```

Contains reference implementations.

Current:

```text
job-application-platform
```

Future:

```text
music-catalog-platform
ecommerce-platform
java-job-application-platform
```

---

```text
docs/
```

Contains the engineering knowledge base inside the repo.

This includes:

```text
requirements
user stories
acceptance criteria
setup notes
runbooks
troubleshooting
architecture
diagrams
Obsidian planning
```

---

```text
infra/
```

Reserved for future infrastructure assets.

Expected later:

```text
Docker Compose
Kubernetes YAML
Prometheus config
Grafana dashboards
Helm charts
```

---

```text
scripts/
```

Reserved for repeatable setup/deploy/test scripts.

Expected later:

```text
environment setup
Git helpers
deployment helpers
validation scripts
```

---

## Why This Layout Works

The root repo represents the reusable platform:

```text
motorweb = Modern Web Platform
```

The first app is only one reference implementation:

```text
apps/job-application-platform
```

This allows the platform to grow beyond Python and beyond the job app domain.
