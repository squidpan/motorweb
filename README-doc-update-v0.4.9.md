# README Update - v0.4.9 Logging Foundation Addendum

Add this section after the Quick Start / API validation sections in the root `README.md`.

---

## Logging Foundation

`motorweb` treats logging as a first-class platform capability.

Logging must support:

```text
testing
troubleshooting
deployment
operations
future monitoring
```

The logging foundation is documented in:

```text
docs/logging/
```

Start with:

```text
docs/logging/logging-strategy.md
docs/logging/logging-fields-standard.md
docs/logging/log-levels-and-events.md
docs/logging/testing-troubleshooting-deployment-logs.md
docs/logging/local-stdout-logging.md
docs/logging/future-structured-json-logging.md
```

Runbooks and troubleshooting:

```text
docs/runbooks/validate-application-logs.md
docs/troubleshooting/logging-troubleshooting.md
```

Reserved app structure:

```text
apps/job-application-platform/app/core/
apps/job-application-platform/logs/examples/
```

Reserved future monitoring structure:

```text
infra/monitoring/logging/
```

Current design rule:

```text
Log to stdout first.
Do not start with application log files.
```

Reason:

```text
local terminal
Docker logs
Kubernetes logs
future Loki/Grafana log collection
```

All applications under `motorweb` should eventually follow the same logging convention so logs can be searched across apps and languages.
