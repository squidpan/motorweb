# motorweb
## Modern Web Platform

`motorweb` is a long-term engineering learning platform for building, testing, deploying, documenting, and operating modern web applications.

The first reference implementation is:

```text
apps/job-application-platform/
```

The first implementation uses:

```text
Python
FastAPI
Uvicorn
JSON/CSV flat-file storage
pytest
curl/Postman testing
```

Later implementations may include:

```text
PostgreSQL
Docker
Kubernetes
Prometheus
Grafana
OAuth2/JWT
Cloud deployment
Java/Spring Boot
Music catalog APIs
E-commerce APIs
```

---

# 1. Quick Start - Run the Job Application Platform

Start here after cloning/extracting the repo.

## 1.1 Go to the app folder

```bash
cd /opt/projects/motorweb/apps/job-application-platform
```

Or, if you are still working from your home folder:

```bash
cd ~/pjs/repos/PycharmProjects/motorweb/apps/job-application-platform
```

## 1.2 Create Python virtual environment

```bash
python3.13 -m venv .venv
```

## 1.3 Activate virtual environment

```bash
source .venv/bin/activate
```

You should see something like:

```text
(.venv)
```

in your shell prompt.

## 1.4 Install dependencies

```bash
pip install -r requirements.txt
```

## 1.5 Run the API

```bash
uvicorn app.main:app --reload
```

Open Swagger/OpenAPI docs:

```text
http://127.0.0.1:8000/docs
```

If port `8000` is already used:

```bash
uvicorn app.main:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001/docs
```

---

# 2. Quick API Validation

## 2.1 Health check

```bash
curl http://127.0.0.1:8000/health
```

Expected:

```json
{"status":"ok"}
```

## 2.2 Get jobs

```bash
curl http://127.0.0.1:8000/jobs
```

## 2.3 Check active storage backend

```bash
curl http://127.0.0.1:8000/storage
```

---

# 3. Storage Backend Modes

The app supports configurable flat-file storage.

## 3.1 JSON backend

```bash
export JOBAPP_STORAGE_BACKEND=json
uvicorn app.main:app --reload
```

## 3.2 CSV backend

```bash
export JOBAPP_STORAGE_BACKEND=csv
uvicorn app.main:app --reload
```

The design goal is:

```text
API layer stays stable
Service layer stays stable
Repository backend can change
```

Storage roadmap:

```text
JSON / CSV
    ↓
SQLite
    ↓
PostgreSQL
    ↓
future distributed stores if useful
```

---

# 4. Project Layout

```text
motorweb/
├── apps/
│   └── job-application-platform/
│       ├── app/
│       ├── tests/
│       ├── scripts/
│       ├── Dockerfile
│       ├── README.md
│       ├── pyproject.toml
│       └── requirements.txt
│
├── docs/
│   ├── setup/
│   ├── git/
│   ├── linux-users/
│   ├── environments/
│   ├── requirements/
│   ├── user-stories/
│   ├── acceptance-criteria/
│   ├── api-design/
│   ├── testing/
│   ├── troubleshooting/
│   ├── runbooks/
│   ├── diagrams/
│   └── obsidian/
│
├── infra/
│   ├── docker/
│   ├── k8s/
│   └── monitoring/
│
└── scripts/
```

---

# 5. Documentation Map

Use this section to find the right documentation quickly.

## 5.1 Initial setup

```text
docs/setup/01-github-multiple-ssh-accounts.md
docs/setup/02-initial-github-push.md
docs/setup/03-linux-users-service-accounts.md
docs/setup/04-post-setup-troubleshooting-links.md
docs/setup/05-shared-opt-projects-model.md
docs/setup/06-branch-merge-doc-updates.md
```

## 5.2 Environment model

```text
docs/environments/dev-test-prod-access-model.md
```

## 5.3 Troubleshooting

```text
docs/troubleshooting/README.md
docs/troubleshooting/git-and-ssh.md
docs/troubleshooting/linux-permissions-and-groups.md
docs/troubleshooting/shared-repo-workflow.md
docs/troubleshooting/opt-projects-permissions.md
```

## 5.4 Runbooks

```text
docs/runbooks/initial-setup-validation-runbook.md
docs/runbooks/reclone-motorweb-under-opt-projects.md
```

## 5.5 Diagrams

```text
docs/diagrams/README.md
docs/diagrams/plantuml/
docs/diagrams/drawio/
docs/diagrams/images/
docs/diagrams/exports/
docs/diagrams/json/
docs/diagrams/yaml/
```

## 5.6 Business analysis docs

```text
docs/requirements/
docs/user-stories/
docs/acceptance-criteria/
docs/api-design/
docs/testing/
```

## 5.7 Obsidian planning

```text
docs/obsidian/
```

---

# 6. GitHub and SSH Setup

This repo is intended to use GitHub SSH access.

Primary account:

```text
squidpan
```

Secondary account:

```text
paulchlyu
```

Recommended SSH aliases:

```text
github-squidpan
github-paulchlyu
```

Main repo remote:

```bash
git@github-squidpan:squidpan/motorweb.git
```

Setup guide:

```text
docs/setup/01-github-multiple-ssh-accounts.md
```

Common issues:

```text
docs/troubleshooting/git-and-ssh.md
```

---

# 7. Recommended Local Repo Location

The intended shared local repo location is:

```text
/opt/projects/motorweb
```

Shared source-code model:

```text
pl  = senior developer + sudo/admin
dev = regular developer
ted = deploy/test operator
```

Both `pl` and `dev` should be able to create, modify, commit, and manage files under:

```text
/opt/projects
```

`ted` should not modify source repositories.

Recommended ownership:

```text
/opt/projects
owner: dev
group: developers
mode: 2775
```

Expected:

```bash
ls -ld /opt/projects
```

```text
drwxrwsr-x dev developers /opt/projects
```

Detailed guide:

```text
docs/setup/05-shared-opt-projects-model.md
```

Troubleshooting:

```text
docs/troubleshooting/opt-projects-permissions.md
```

---

# 8. Linux User and Environment Model

Human users:

```text
pl   = senior developer + sudo/admin
dev  = regular developer
ted  = deploy/test operator
```

Service accounts:

```text
svc-dev
svc-test
svc-prod
```

Environment groups:

```text
env-dev
env-test
env-prod
```

Environment folders:

```text
/opt/envs/dev/motorweb
/opt/envs/test/motorweb
/opt/envs/prod/motorweb
```

Release folder:

```text
/opt/releases/motorweb
```

Setup guide:

```text
docs/setup/03-linux-users-service-accounts.md
```

Environment model:

```text
docs/environments/dev-test-prod-access-model.md
```

---

# 9. Recommended Git Workflow

## 9.1 Check current branch

```bash
cd /opt/projects/motorweb
git status
```

## 9.2 Create a feature branch using modern Git syntax

```bash
git switch -c feature/my-change
```

## 9.3 Add and commit

```bash
git add .
git commit -m "Describe the change"
```

## 9.4 Push branch

```bash
git push -u origin feature/my-change
```

## 9.5 Merge back to main locally

```bash
git switch main
git pull
git merge feature/my-change
git push origin main
```

More details:

```text
docs/setup/06-branch-merge-doc-updates.md
```

---

# 10. Applying Documentation Overlay Packages

For a docs-only zip update:

```bash
cd /opt/projects/motorweb
git switch main
git pull
git switch -c feature/docs-update
unzip ~/Downloads/<doc-update-package>.zip -d .
git status
git diff --stat
git add .
git commit -m "Update documentation"
git push -u origin feature/docs-update
```

Merge:

```bash
git switch main
git pull
git merge feature/docs-update
git push origin main
```

---

# 11. Common Troubleshooting Quick Reference

## 11.1 SSH agent has no identities

```bash
ssh-add -l
ssh-add ~/.ssh/id_ed25519_squidpan
```

See:

```text
docs/troubleshooting/git-and-ssh.md
```

## 11.2 GitHub permission denied publickey

```bash
ssh -T github-squidpan
cat ~/.ssh/config
ssh-add -l
```

See:

```text
docs/troubleshooting/git-and-ssh.md
```

## 11.3 Git remote origin already exists

```bash
git remote -v
git remote set-url origin git@github-squidpan:squidpan/motorweb.git
```

See:

```text
docs/troubleshooting/git-and-ssh.md
```

## 11.4 Git dubious ownership

```bash
git config --global --add safe.directory /opt/projects/motorweb
```

See:

```text
docs/troubleshooting/linux-permissions-and-groups.md
```

## 11.5 Git index.lock permission denied

```bash
id
newgrp developers
cd /opt/projects/motorweb
git add .
```

See:

```text
docs/troubleshooting/opt-projects-permissions.md
```

## 11.6 Port 8000 already in use

Use another port:

```bash
uvicorn app.main:app --reload --port 8001
```

Or find the process:

```bash
ss -tulpen | grep 8000
```

---

# 12. PlantUML, draw.io, and Architecture Diagrams

Diagram sources live under:

```text
docs/diagrams/
```

PlantUML examples:

```text
docs/diagrams/plantuml/jobapp-context.puml
docs/diagrams/plantuml/job-create-sequence.puml
docs/diagrams/plantuml/linux-users-env-access.puml
```

Can PlantUML be generated from Python source?

Partially.

Good candidates:

```text
class diagrams
package/module diagrams
dependency diagrams
```

Usually better manually designed:

```text
sequence diagrams
architecture diagrams
deployment diagrams
business process flows
Kubernetes diagrams
```

See:

```text
docs/diagrams/README.md
```

---

# 13. Business Analysis Perspective

This project includes business analysis artifacts because the goal is not just coding.

Planned/active BA docs:

```text
requirements
user stories
acceptance criteria
API contracts
test scenarios
process flows
runbooks
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

# 14. Obsidian Knowledge Base Strategy

Recommended master skill / topic:

```text
Modern Web Platform
```

Also described as:

```text
Modern Web Application Platform Engineering
```

First use case:

```text
Job Application Platform
```

The implementation repo and the Obsidian knowledge base should evolve together.

Suggested Obsidian note domains:

```text
requirements
user stories
acceptance criteria
REST APIs
FastAPI
PostgreSQL
Docker
Kubernetes
monitoring
networking
observability
deployment
testing
troubleshooting
runbooks
```

---

# 15. Development Roadmap

## Phase 1 - Current

```text
FastAPI app
CRUD endpoints
JSON storage
CSV storage
Swagger docs
curl/Postman testing
Git/GitHub setup
Linux multiuser setup
```

## Phase 2 - Documentation hardening

```text
README consolidation
setup docs
troubleshooting docs
runbooks
BA docs
diagram structure
```

## Phase 3 - Database

```text
SQLite
PostgreSQL
SQLAlchemy
Alembic
```

## Phase 4 - Containerization

```text
Dockerfile refinement
Docker Compose
API + database containers
```

## Phase 5 - Kubernetes

```text
namespace
deployment
service
configmap
secret
ingress
```

## Phase 6 - Monitoring

```text
Prometheus
Grafana
health checks
readiness/liveness probes
```

## Phase 7 - Auth

```text
OAuth2
JWT
RBAC
```

## Phase 8 - Cloud / Homelab

```text
Proxmox
k3s/kind/k8s
AWS
Google Cloud
```

---

# 16. Golden Rules

1. Keep working app code stable.
2. Use branches for changes.
3. `pl` and `dev` can modify source.
4. `ted` deploys/tests from releases, not source.
5. Do not use `sudo git`.
6. Prefer terminal commands over GUI copy/paste for `/opt/projects`.
7. Document every real failure in `docs/troubleshooting`.
8. Keep README useful as the main entry point.1G
