# Testing, Troubleshooting, and Deployment Logs

Logging should support three major use cases.

---

## 1. Testing logs

Testing logs help answer:

```text
Did the test hit the expected endpoint?
Did the app use the expected storage backend?
Did the request return the expected status code?
Did a validation error occur?
```

Useful events:

```text
request_started
request_completed
request_failed
job_created
job_updated
job_deleted
storage_backend_selected
```

Testing examples:

```text
curl tests
Postman/Insomnia tests
pytest tests
future CI/CD tests
```

---

## 2. Troubleshooting logs

Troubleshooting logs help answer:

```text
Why did the request fail?
Which component failed?
Was it router, service, repository, storage, config, or environment?
What request_id should I search for?
```

Useful fields:

```text
request_id
event
error_type
error_message
component
operation
path
status_code
duration_ms
storage_backend
```

---

## 3. Deployment logs

Deployment logs help answer:

```text
Which version started?
Which environment is running?
Which storage backend is configured?
Did the service start correctly?
Is the health endpoint working?
```

Useful events:

```text
service_startup
version_loaded
config_loaded
storage_backend_selected
storage_ready
health_check_passed
```

---

## Deployment validation checklist

After deployment, logs should show:

```text
[INFO] service_startup
[INFO] config_loaded
[INFO] version_loaded
[INFO] storage_backend_selected
[INFO] storage_ready
[INFO] health_check_passed
```

If any startup requirement fails, logs should show:

```text
[ERROR] or [CRITICAL]
```

with a clear event name and component.
