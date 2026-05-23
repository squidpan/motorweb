# Logging Fields Standard

This document defines common log fields for `motorweb`.

---

## Required common fields

| Field | Meaning | Example |
|---|---|---|
| `timestamp` | When event happened | `2026-05-22T18:30:10Z` |
| `level` | Log severity | `INFO` |
| `service` | Application/service name | `job-application-platform` |
| `environment` | Runtime environment | `dev` |
| `event` | Machine-friendly event name | `request_completed` |
| `message` | Human-friendly message | `Request completed` |

---

## Request fields

| Field | Meaning | Example |
|---|---|---|
| `request_id` | Unique ID for one request | `abc123` |
| `method` | HTTP method | `GET` |
| `path` | HTTP path | `/jobs` |
| `status_code` | HTTP status | `200` |
| `duration_ms` | Request duration | `8` |
| `client_ip` | Caller IP if useful | `127.0.0.1` |

---

## Application fields

| Field | Meaning | Example |
|---|---|---|
| `version` | App version | `0.1.0` |
| `storage_backend` | Active repository backend | `json` |
| `component` | App component | `repository` |
| `operation` | Business operation | `create_job` |

---

## Error fields

| Field | Meaning | Example |
|---|---|---|
| `error_type` | Exception/error class | `ValueError` |
| `error_message` | Error summary | `Invalid job id` |
| `stack_trace` | Stack trace, usually dev only | optional |
| `failed_component` | Component where failure occurred | `job_repository` |

---

## Future auth/audit fields

Add later when authentication exists:

| Field | Meaning |
|---|---|
| `user_id` | Authenticated user |
| `role` | User role |
| `tenant_id` | Tenant/customer if multi-tenant |
| `auth_event` | login/logout/token event |

---

## Future tracing fields

Add later when distributed tracing exists:

| Field | Meaning |
|---|---|
| `trace_id` | Distributed trace ID |
| `span_id` | Current span |
| `correlation_id` | Business or workflow correlation ID |

---

## Naming convention

Use snake_case event names:

```text
service_startup
config_loaded
storage_backend_selected
request_started
request_completed
request_failed
job_created
job_updated
job_deleted
health_check_passed
```
