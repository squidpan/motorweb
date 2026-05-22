# Dev/Test/Prod Access Model

## Human Users

```text
pl   = admin/sudo
dev  = developer
ted  = test/deploy operator
```

## Service Accounts

```text
svc-dev   = owns/runs dev environment
svc-test  = owns/runs test environment
svc-prod  = owns/runs prod environment
```

## Access Matrix

| User | Source Repo | Dev Env | Test Env | Prod Env |
|---|---|---|---|---|
| pl | full | full | full | full |
| dev | full | full | optional | normally no |
| ted | read-only/no-write | optional | deploy/test | deploy/test if granted |
| svc-dev | no human use | runtime owner | no | no |
| svc-test | no human use | no | runtime owner | no |
| svc-prod | no human use | no | no | runtime owner |

## Promotion Flow

```text
dev source repo
    ↓ tag release
GitHub tag
    ↓ clone/read-only deploy
/opt/releases
    ↓ deploy
/opt/envs/test
    ↓ promote
/opt/envs/prod
```

## Key Rules

1. `dev` and `pl` can modify source.
2. `ted` deploys from tags.
3. `ted` should not edit source repositories.
4. Service accounts own runtime folders.
5. Environment access is controlled with Linux groups.
6. Prod access can be granted or removed using `env-prod`.

## Future Kubernetes Mapping

```text
dev  → namespace: mwp-dev
test → namespace: mwp-test
prod → namespace: mwp-prod
```
