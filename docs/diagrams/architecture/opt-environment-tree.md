# `/opt` Environment Tree Diagram

```text
/opt
│
├── projects
│   └── motorweb
│       └── active source repo
│
├── releases
│   └── motorweb
│       ├── v0.1.0
│       ├── v0.2.0
│       └── current -> v0.2.0
│
└── envs
    ├── dev
    │   └── motorweb
    │
    ├── test
    │   └── motorweb
    │
    └── prod
        └── motorweb
```

## Ownership Intent

```text
/opt/projects/motorweb   pl:developers
/opt/releases/motorweb   ted:deployers
/opt/envs/dev/motorweb   pl:env-dev
/opt/envs/test/motorweb  svc-test:env-test
/opt/envs/prod/motorweb  svc-prod:env-prod
```
