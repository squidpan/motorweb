# README Update - v0.4.2 Documentation Addendum

Add this section to the root `README.md` after the initial setup section.

---

## Shared `/opt/projects` Development Model

The `motorweb` repository is now intended to live under:

```text
/opt/projects/motorweb
```

The shared development model is:

```text
pl  = senior developer + sudo/admin
dev = regular developer
ted = deploy/test operator
```

Both `pl` and `dev` should be able to create, modify, commit, and manage files under `/opt/projects`.

`ted` should not modify source repositories. `ted` should deploy and test from tagged releases under `/opt/releases`, `/opt/envs/test`, and `/opt/envs/prod`.

Recommended ownership for `/opt/projects`:

```text
owner: dev
group: developers
mode: 2775
```

Expected:

```bash
ls -ld /opt/projects
```

```text
drwxrwsr-x dev developers /opt/projects
```

See:

```text
docs/setup/05-shared-opt-projects-model.md
docs/setup/06-branch-merge-doc-updates.md
docs/runbooks/reclone-motorweb-under-opt-projects.md
docs/troubleshooting/opt-projects-permissions.md
```
