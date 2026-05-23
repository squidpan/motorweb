# Example Log Lines

## Service startup

```text
2026-05-22T18:30:10Z [INFO] service_startup service=job-application-platform env=dev version=0.1.0 message="Service starting"
```

## Config loaded

```text
2026-05-22T18:30:10Z [INFO] config_loaded service=job-application-platform env=dev storage_backend=json message="Configuration loaded"
```

## Storage backend selected

```text
2026-05-22T18:30:11Z [INFO] storage_backend_selected service=job-application-platform env=dev storage_backend=json message="Using JSON repository backend"
```

## Request completed

```text
2026-05-22T18:30:15Z [INFO] request_completed service=job-application-platform env=dev request_id=abc123 method=GET path=/jobs status=200 duration_ms=8 message="Request completed"
```

## Slow request

```text
2026-05-22T18:31:00Z [WARNING] slow_request service=job-application-platform env=dev request_id=def456 method=GET path=/jobs status=200 duration_ms=1250 message="Request exceeded slow threshold"
```

## Request failed

```text
2026-05-22T18:31:40Z [ERROR] request_failed service=job-application-platform env=dev request_id=ghi789 method=POST path=/jobs status=500 error_type=ValueError message="Request failed"
```

## Repository write failed

```text
2026-05-22T18:32:10Z [ERROR] storage_write_failed service=job-application-platform env=dev component=job_repository storage_backend=csv error_type=PermissionError message="Could not write jobs.csv"
```
