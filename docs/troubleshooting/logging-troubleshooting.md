# Logging Troubleshooting

## No logs appear

Check that the app is running in the current terminal:

```bash
uvicorn app.main:app --reload
```

If running under Docker or Kubernetes later, use:

```bash
docker logs <container>
kubectl logs <pod>
```

---

## Logs do not show request_id

Likely cause:

```text
request logging middleware not enabled
```

Future fix:

```text
enable request_logging_middleware
```

---

## Logs are too noisy

Likely cause:

```text
log level set to DEBUG
```

Use INFO for normal local development.

---

## Logs are missing storage backend

Likely cause:

```text
startup/config logging does not include storage_backend
```

Expected startup event:

```text
storage_backend_selected
```

---

## Sensitive data in logs

Do not log:

```text
passwords
tokens
secret keys
full auth headers
personal data unless explicitly needed and safe
```

Later, add redaction rules for auth and headers.
