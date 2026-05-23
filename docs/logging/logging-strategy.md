# Logging Strategy

## Goal

Every application in `motorweb` should emit logs in a common convention.

The goal is to make logs useful for:

```text
testing
troubleshooting
deployment validation
operations
monitoring
future incident response
```

---

## Why logging matters

Logging answers questions such as:

```text
Did the app start correctly?
Which storage backend is active?
Which endpoint was called?
How long did the request take?
Did the request fail?
What error occurred?
Which version was deployed?
Was the service ready?
```

---

## Current approach

Start simple:

```text
human-readable logs to stdout
```

Example:

```text
2026-05-22T18:30:10Z [INFO] service_startup service=job-application-platform env=dev storage=json version=0.1.0
2026-05-22T18:30:15Z [INFO] request_completed request_id=abc123 method=GET path=/jobs status=200 duration_ms=8
2026-05-22T18:31:02Z [WARNING] storage_file_missing file=jobs.json action=create_empty_file
2026-05-22T18:31:40Z [ERROR] request_failed request_id=def456 method=POST path=/jobs status=500 error_type=ValueError
```

---

## Future approach

Move toward structured JSON logs:

```json
{
  "timestamp": "2026-05-22T18:30:15Z",
  "level": "INFO",
  "service": "job-application-platform",
  "environment": "dev",
  "event": "request_completed",
  "request_id": "abc123",
  "method": "GET",
  "path": "/jobs",
  "status_code": 200,
  "duration_ms": 8
}
```

---

## Core design rule

```text
Application code should not care where logs eventually go.
```

The application emits logs to stdout.

Later, the runtime platform collects them:

```text
terminal
Docker logs
Kubernetes logs
Loki
Grafana
ELK/OpenSearch
cloud logging
```

---

## Logging should be consistent across languages

Future apps may include:

```text
Python/FastAPI
Java/Spring Boot
Node.js
Go
```

They should all use the same event naming and field conventions where practical.
