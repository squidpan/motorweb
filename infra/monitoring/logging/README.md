# Monitoring - Logging

Reserved for future logging/observability infrastructure.

Possible future tools:

```text
Loki
Promtail
Grafana
ELK / OpenSearch
Cloud logging
```

Current app rule:

```text
emit logs to stdout
```

Future collection path:

```text
app stdout
  ↓
Docker/Kubernetes logs
  ↓
log collector
  ↓
Grafana or search UI
```
