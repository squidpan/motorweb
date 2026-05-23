# Local stdout Logging

## Current rule

For now, log to stdout.

Do not start with app-managed log files.

---

## Why stdout?

stdout works naturally with:

```text
local terminal
Tilix
PyCharm run console
Docker logs
Kubernetes logs
future log collectors
```

Modern container platforms expect applications to write logs to stdout/stderr.

---

## Local development

Run:

```bash
cd /opt/projects/motorweb/apps/job-application-platform
source .venv/bin/activate
uvicorn app.main:app --reload
```

Expected future logs should appear in the terminal.

---

## Future Docker

Later:

```bash
docker logs <container>
```

should show the same application logs.

---

## Future Kubernetes

Later:

```bash
kubectl logs deployment/job-application-api
```

should show the same application logs.

---

## Future log collection

Later collection path:

```text
app stdout
  ↓
container runtime
  ↓
Kubernetes logs
  ↓
Loki / ELK / cloud logging
  ↓
Grafana dashboards
```
