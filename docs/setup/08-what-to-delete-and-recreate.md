# 08 - What To Delete and Recreate

This document explains what should and should not be deleted when switching to the simplified laptop model.

---

## Do not delete

Do not delete SSH keys:

```text
/home/pl/.ssh/id_ed25519_squidpan
/home/pl/.ssh/id_ed25519_squidpan.pub
/home/pl/.ssh/id_ed25519_paulchlyu
/home/pl/.ssh/id_ed25519_paulchlyu.pub
/home/pl/.ssh/config
```

Do not delete GitHub repositories.

Do not delete pushed work from GitHub.

---

## Usually do not delete dev

You do not need to delete the `dev` Linux user.

It can remain unused for now.

Reasons to keep:

```text
future second developer simulation
future permission experiments
no harm if unused
```

If you really want to delete it later, first make sure it does not own anything important.

Check:

```bash
find /opt -user dev -ls
```

---

## Do not delete ted

Keep `ted` for later deploy/test practice.

`ted` is useful for:

```text
tagged release deployment
test environment validation
prod-like deployment simulation
```

---

## `/opt/projects`

You do not need to delete `/opt/projects`.

Recommended repair:

```bash
sudo chown -R pl:developers /opt/projects
sudo chmod -R g+rwX /opt/projects
sudo find /opt/projects -type d -exec chmod 2775 {} \;
sudo setfacl -R -m u:pl:rwx,g:developers:rwx /opt/projects
sudo setfacl -R -d -m u:pl:rwx,g:developers:rwx /opt/projects
```

---

## When to delete `/opt/projects/motorweb`

Delete and reclone only if:

```text
permissions are too messy
local repo has no important uncommitted changes
important work has already been pushed to GitHub
```

Before deleting:

```bash
cd /opt/projects/motorweb
git status
git remote -v
```

If needed, save local changes:

```bash
git diff > ~/motorweb-local-changes.patch
```

Delete and reclone:

```bash
cd /opt/projects
sudo rm -rf motorweb
git clone git@github-squidpan:squidpan/motorweb.git
sudo chown -R pl:developers /opt/projects/motorweb
sudo chmod -R g+rwX /opt/projects/motorweb
sudo find /opt/projects/motorweb -type d -exec chmod 2775 {} \;
```

---

## Recommended final state

```text
/opt/projects              pl:developers
/opt/projects/motorweb     pl:developers
/opt/releases              ted:deployers
/opt/envs/dev              pl:env-dev
/opt/envs/test             svc-test:env-test
/opt/envs/prod             svc-prod:env-prod
```
