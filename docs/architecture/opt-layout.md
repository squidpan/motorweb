# `/opt` Folder Layout for motorweb

This document explains the Linux workstation layout used for the simplified laptop model.

---

## Target `/opt` Layout

```text
/opt/
├── projects/
│   └── motorweb/
│       ├── apps/
│       │   └── job-application-platform/
│       ├── docs/
│       ├── infra/
│       └── scripts/
│
├── releases/
│   └── motorweb/
│       ├── v0.1.0/
│       ├── v0.2.0/
│       └── current -> v0.2.0
│
└── envs/
    ├── dev/
    │   └── motorweb/
    ├── test/
    │   └── motorweb/
    └── prod/
        └── motorweb/
```

---

## Meaning

```text
/opt/projects/motorweb
```

Active source-code working repo.

Owner model:

```text
pl:developers
```

---

```text
/opt/releases/motorweb
```

Tagged release clones or packaged release artifacts.

Later used by:

```text
ted
```

---

```text
/opt/envs/dev/motorweb
/opt/envs/test/motorweb
/opt/envs/prod/motorweb
```

Runtime/deployment locations.

Later these map conceptually to Kubernetes namespaces:

```text
mwp-dev
mwp-test
mwp-prod
```

---

## Simplified Laptop Model

```text
pl  = primary developer + sudo/admin
ted = deploy/test operator later
dev = optional future developer
```

Active development belongs to:

```text
pl
```

Deployment/testing later belongs to:

```text
ted
service accounts
environment groups
```
