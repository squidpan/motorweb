# Local Release Deployment Flow

This document describes the local deploy/test flow before GitLab CI/CD and cloud deployment.

## Current flow

```text
pl develops
  ↓
pl merges to main
  ↓
pl cuts Git tag
  ↓
ted clones tag under /opt/releases
  ↓
ted creates venv
  ↓
ted runs dataload
  ↓
ted starts FastAPI app
  ↓
ted validates curl endpoints
```

## Why this matters

This creates the foundation for future CI/CD.

Later, the same flow becomes:

```text
GitLab tag pipeline
  ↓
run tests
  ↓
build Docker image
  ↓
push container registry
  ↓
deploy test
  ↓
manual approval
  ↓
deploy prod/cloud
```

## Current deployment artifact

Today:

```text
Git tag + source checkout
```

Future:

```text
Container image
```

## Current runtime

Today:

```text
Python venv + Uvicorn
```

Future:

```text
Docker
Kubernetes
Cloud Run
```
