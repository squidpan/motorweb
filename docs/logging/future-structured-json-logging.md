# Future Structured JSON Logging

Readable text logs are good for local development.

Structured JSON logs are better for automated search and monitoring.

---

## Why JSON logs?

JSON logs are easier to query by fields:

```text
service
environment
event
request_id
status_code
duration_ms
error_type
```

Example future query:

```text
show all ERROR logs for job-application-platform in test
```

or:

```text
show all requests slower than 500ms
```

---

## Example JSON log

```json
{
  "timestamp": "2026-05-22T18:30:15Z",
  "level": "INFO",
  "service": "job-application-platform",
  "environment": "dev",
  "version": "0.1.0",
  "event": "request_completed",
  "request_id": "abc123",
  "method": "GET",
  "path": "/jobs",
  "status_code": 200,
  "duration_ms": 8,
  "message": "Request completed"
}
```

---

## Recommended transition

Phase 1:

```text
human-readable stdout logs
```

Phase 2:

```text
configurable format: text or json
```

Phase 3:

```text
JSON logs in Docker/Kubernetes
```

Phase 4:

```text
Loki/Grafana or ELK/OpenSearch integration
```
