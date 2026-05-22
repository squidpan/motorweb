# Simplified Permissions Troubleshooting

This document supports the simplified laptop model where `pl` owns active development.

---

## Correct active repo ownership

Expected:

```bash
ls -ld /opt/projects
ls -ld /opt/projects/motorweb
```

Expected pattern:

```text
drwxrwsr-x pl developers /opt/projects
drwxrwsr-x pl developers /opt/projects/motorweb
```

---

## venv creation permission denied

### Symptom

```bash
python3.13 -m venv .venv
```

Output:

```text
Error: [Errno 13] Permission denied: '.venv'
```

### Likely cause

The repo or app folder is owned by another user, commonly:

```text
dev:developers
```

or has inconsistent nested permissions.

### Fix

```bash
sudo chown -R pl:developers /opt/projects/motorweb
sudo chmod -R g+rwX /opt/projects/motorweb
sudo find /opt/projects/motorweb -type d -exec chmod 2775 {} \;
sudo setfacl -R -m u:pl:rwx,g:developers:rwx /opt/projects/motorweb
sudo setfacl -R -d -m u:pl:rwx,g:developers:rwx /opt/projects/motorweb
```

Then:

```bash
cd /opt/projects/motorweb/apps/job-application-platform
rm -rf .venv
python3.13 -m venv .venv
```

---

## Downloaded zip files are owned by pl

This is normal.

Most files downloaded from ChatGPT or browser will be owned by:

```text
pl:pl
```

That is why the active source repo should also be easy for `pl` to write to.

---

## Do I need `newgrp developers`?

Only if your current shell does not show `developers`.

Check:

```bash
id
```

If missing:

```bash
newgrp developers
```

Permanent fix:

```text
log out and log back in
```

---

## Should I delete dev?

Usually no.

`dev` can remain as an unused future account.

If you later want to simulate a second developer, add `dev` to `developers` and use the same group model.

---

## Should ted have access to source?

No.

`ted` should not be in `developers`.

`ted` should work later from:

```text
/opt/releases/motorweb
/opt/envs/test/motorweb
/opt/envs/prod/motorweb
```

---

## Golden rule

For laptop learning:

```text
pl owns active development.
ted tests/deploys releases later.
dev is optional/future.
```
