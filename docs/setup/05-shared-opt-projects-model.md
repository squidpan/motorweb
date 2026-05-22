# 05 - Shared `/opt/projects` Model

This document defines the final intended shared source repository model for `motorweb`.

## Goal

Use `/opt/projects` as the shared source-code area where both `pl` and `dev` can work as developers.

`ted` should not modify source repositories.

## User Roles

```text
pl  = senior developer + sudo/admin
dev = regular developer
ted = deploy/test operator
```

## Intended Access

| User | `/opt/projects` | `/opt/projects/motorweb` | Purpose |
|---|---|---|---|
| pl | read/write | read/write | senior dev + admin |
| dev | read/write | read/write | regular dev |
| ted | no write | no write | deploy/test from releases |

## Required Groups

`pl` and `dev` must be in:

```text
developers
```

`ted` should not be in `developers`.

Check:

```bash
id pl
id dev
id ted
```

## Create or repair `/opt/projects`

Run as `pl`:

```bash
sudo mkdir -p /opt/projects
sudo chown dev:developers /opt/projects
sudo chmod 2775 /opt/projects
```

Optional but recommended ACL defaults:

```bash
sudo setfacl -m g:developers:rwx /opt/projects
sudo setfacl -d -m g:developers:rwx /opt/projects
```

## Expected permissions

```bash
ls -ld /opt/projects
```

Expected:

```text
drwxrwsr-x dev developers ... /opt/projects
```

The `s` means setgid is enabled. New folders created under `/opt/projects` inherit the `developers` group.

## Why owner is `dev`

The directory is owned by `dev:developers` because `dev` is the canonical developer owner.

But `pl` has the same source-code access because `pl` belongs to `developers`.

Effective model:

```text
pl  = full developer access + admin
dev = full developer access
ted = no source write
```

## Avoid GUI copy/paste for shared repos

Do not use the Pop!_OS file manager to copy active repositories into `/opt/projects`.

GUI copy/paste may create files as `pl:pl` or preserve inconsistent permissions.

Use terminal commands instead:

```bash
cd /opt/projects
git clone git@github-squidpan:squidpan/motorweb.git
sudo chown -R dev:developers motorweb
sudo chmod -R g+rwX motorweb
sudo find motorweb -type d -exec chmod 2775 {} \\;
sudo setfacl -R -m g:developers:rwx motorweb
sudo setfacl -R -d -m g:developers:rwx motorweb
```

## Safe directory note

Because the repo may be owned by `dev` while `pl` works in it, Git may show:

```text
fatal: detected dubious ownership
```

Fix for trusted local repo:

```bash
git config --global --add safe.directory /opt/projects/motorweb
```

## Current recommended source repo location

```text
/opt/projects/motorweb
```

Avoid keeping two active working copies such as:

```text
~/pjs/repos/PycharmProjects/motorweb
/opt/projects/motorweb
```
