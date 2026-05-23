# Runbook - Validate Application Logs

Use this runbook after the logging implementation is added.

For now, this documents the expected future validation process.

---

## 1. Start API

```bash
cd /opt/projects/motorweb/apps/job-application-platform
source .venv/bin/activate
uvicorn app.main:app --reload
```

---

## 2. Confirm startup logs

Expected events:

```text
service_startup
config_loaded
version_loaded
storage_backend_selected
storage_ready
```

---

## 3. Send health request

```bash
curl http://127.0.0.1:8000/health
```

Expected log event:

```text
request_completed method=GET path=/health status=200
```

---

## 4. Send jobs request

```bash
curl http://127.0.0.1:8000/jobs
```

Expected log event:

```text
request_completed method=GET path=/jobs status=200
```

---

## 5. Trigger bad request later

When validation exists, send a bad payload.

Expected log event:

```text
request_failed
job_validation_failed
```

---

## 6. Validate log fields

Each request log should include:

```text
timestamp
level
service
environment
event
request_id
method
path
status_code
duration_ms
message
```
