# Log Levels and Events

This document defines standard logging levels and common events.

---

## Log levels

### DEBUG

Detailed information useful during development.

Examples:

```text
repository_read_started
repository_write_completed
parsed_job_payload
```

Use carefully. Do not log secrets or sensitive payloads.

---

### INFO

Normal successful events.

Examples:

```text
service_startup
config_loaded
storage_backend_selected
request_completed
job_created
health_check_passed
```

---

### WARNING

Something unusual happened but the application can continue.

Examples:

```text
storage_file_missing
deprecated_config_used
request_validation_warning
slow_request
```

---

### ERROR

An operation failed.

Examples:

```text
request_failed
storage_write_failed
job_not_found
config_load_failed
```

---

### CRITICAL

The app or process cannot continue.

Examples:

```text
service_startup_failed
required_config_missing
database_unavailable_at_startup
```

---

## Core platform events

### Startup/deployment

```text
service_startup
service_shutdown
config_loaded
version_loaded
storage_backend_selected
storage_ready
health_check_passed
health_check_failed
```

### Request lifecycle

```text
request_started
request_completed
request_failed
slow_request
```

### Job app business events

```text
job_created
job_read
job_updated
job_deleted
job_not_found
job_validation_failed
```

### Repository/storage events

```text
repository_read_started
repository_read_completed
repository_write_started
repository_write_completed
storage_file_missing
storage_write_failed
storage_backend_selected
```

### Future auth/audit events

```text
login_success
login_failed
token_issued
token_expired
access_denied
```

---

## Example readable format

```text
timestamp [LEVEL] event service=... env=... request_id=... message="..."
```

Example:

```text
2026-05-22T18:30:15Z [INFO] request_completed service=job-application-platform env=dev request_id=abc123 method=GET path=/jobs status=200 duration_ms=8
```
