# Logging Architecture

## Current conceptual flow

```text
FastAPI app
  ↓
logging_config
  ↓
stdout
  ↓
terminal / PyCharm / Tilix
```

---

## Future container flow

```text
FastAPI app
  ↓
stdout
  ↓
Docker container logs
  ↓
docker logs
```

---

## Future Kubernetes flow

```text
FastAPI app
  ↓
stdout
  ↓
container runtime
  ↓
kubectl logs
  ↓
Loki / ELK / cloud logging
  ↓
Grafana dashboards
```

---

## Request logging flow

```text
HTTP request
  ↓
request logging middleware
  ↓
generate request_id
  ↓
log request_started
  ↓
route/service/repository
  ↓
log request_completed or request_failed
  ↓
HTTP response
```
