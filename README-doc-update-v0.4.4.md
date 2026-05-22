# README Update - v0.4.4 Simplified User Model Addendum

Replace the earlier shared `/opt/projects` model with this simplified laptop-first model.

---

## Simplified Laptop User Model

For this Pop!_OS laptop learning lab, the active development model is:

```text
pl  = primary developer + sudo/admin
ted = test/deploy operator, later
dev = optional future developer account
```

The active source repository should be owned by `pl`:

```text
/opt/projects/motorweb
owner: pl
group: developers
mode: 2775
```

This avoids daily friction because most downloaded files, ChatGPT zip files, PyCharm work, and terminal work happen as `pl`.

`ted` should not modify source repositories. `ted` should later deploy/test from:

```text
/opt/releases
/opt/envs/test
/opt/envs/prod
```

See:

```text
docs/setup/07-simplified-laptop-user-model.md
docs/runbooks/reset-opt-projects-to-pl-owned.md
docs/troubleshooting/simplified-permissions.md
```
