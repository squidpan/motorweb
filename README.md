# Modern Web Platform (aka motorweb)

This is the baseline engineering repository for building modern Python web applications and REST APIs.

The first reference implementation is:

```text
apps/job-application-platform/
```

This repository supports:

- Job Application Platform as the first use case
- Future Music Catalog Platform use case
- FastAPI REST APIs
- JSON/CSV flat-file persistence
- Future PostgreSQL persistence
- API testing with curl and Postman
- Git/GitHub workflow
- Multiple GitHub accounts using SSH aliases
- Linux multi-user development/deploy model
- Dev/Test/Prod environment model
- Service accounts
- Docker/Kubernetes/monitoring evolution
- PlantUML, draw.io, and architecture diagrams
- Obsidian engineering knowledge base

---

## Immediate Setup Order

### Step 1 — Extract this package

```bash
cd ~/pjs/repos/PycharmProjects
unzip motorweb-baseline-v0.4-platform.zip
cd motorweb
```

### Step 2 — Validate the app locally

```bash
cd apps/job-application-platform
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

If port 8000 is busy:

```bash
uvicorn app.main:app --reload --port 8001
```

### Step 3 — Initialize Git

From the repository root:

```bash
cd ~/pjs/repos/PycharmProjects/motorweb
git init
git add .
git commit -m "Initial validated platform baseline with Job Application Platform"
```

### Step 4 — Set up GitHub SSH access

Follow:

```text
docs/setup/01-github-multiple-ssh-accounts.md
```

### Step 5 — Push to GitHub

Follow:

```text
docs/setup/02-initial-github-push.md
```

### Step 6 — Set up Linux users, groups, and service accounts

Follow:

```text
docs/setup/03-linux-users-service-accounts.md
```

### Step 7 — Review environment access model

Follow:

```text
docs/environments/dev-test-prod-access-model.md
```

---

## Core User Model

Human users:

```text
pl   = admin/sudo user
dev  = developer/test user with full repo access
ted  = test/deploy operator with read-only repo access
```

Service accounts:

```text
svc-dev   = owns/runs dev environment
svc-test  = owns/runs test environment
svc-prod  = owns/runs prod environment
```

Main rule:

```text
pl/dev can modify source repositories.
ted can deploy/test from tagged releases but should not modify source repositories.
```

---

## GitHub Account Model

You have two GitHub accounts:

```text
squidpan
paulchlyu
```

Recommended SSH aliases:

```text
github-squidpan
github-paulchlyu
```

Example main repo remote:

```bash
git remote add origin git@github-squidpan:squidpan/motorweb.git
```

---

## Diagram Strategy

Diagram folders are ready for:

```text
PlantUML
draw.io
PNG/SVG exports
architecture diagrams
sequence diagrams
class diagrams
YAML structure diagrams
JSON payload diagrams
```

See:

```text
docs/diagrams/README.md
```

Yes, PlantUML diagrams can be created from Python source code, but with limits:

- Class diagrams can be partially generated from Python source using tools.
- Sequence diagrams usually need to be designed manually from request flow.
- Architecture diagrams are best maintained manually.
- YAML/JSON diagrams are usually best created from examples/contracts.

---

## Recommended Master Skill Name

```text
Modern Web Platform (aka motorweb)
```

First reference use case:

```text
Job Application Platform
```

Future use cases:

```text
Music Catalog Platform
E-Commerce Platform
Inventory Catalog Platform
```


---

## Naming

```text
motorweb = Modern Web Platform
```

The platform is intentionally technology-agnostic long term.

While the first validated reference implementation is:

```text
apps/job-application-platform
```

using:

```text
Python
FastAPI
```

future reference implementations may include:

```text
Java
Spring Boot
Node.js
Go
```

The Job Application Platform remains the first reference implementation and keeps its current folder name unchanged.

---

## v0.5 Data Load and File-Backed Database Foundation

The Job Application Platform now includes a deliberate file-backed data design.

Key docs:

```text
docs/data/file-backed-database-design.md
docs/runbooks/initial-job-dataload-runbook.md
docs/api-design/jobs-query-api.md
```

App data folders:

```text
apps/job-application-platform/data/dataload/input/
apps/job-application-platform/data/dataload/processed/
apps/job-application-platform/data/database-files/jobs/
apps/job-application-platform/data/schemas/
```

Run initial dataload:

```bash
cd apps/job-application-platform
source .venv/bin/activate
scripts/dataload/run-initial-dataload.sh
scripts/run-json.sh
```

Test:

```bash
curl http://127.0.0.1:8000/jobs
curl 'http://127.0.0.1:8000/jobs?status=Applied'
curl 'http://127.0.0.1:8000/jobs?keyword=Analyst'
```
