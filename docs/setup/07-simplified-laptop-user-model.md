# 07 - Simplified Laptop User Model

This replaces the earlier heavier model where `dev` owned `/opt/projects`.

That model was realistic for a team environment, but too much friction for a single-user learning laptop because most downloaded files and IDE activity happen as `pl`.

---

## Final Recommended Laptop Model

```text
pl  = primary developer + sudo/admin
ted = test/deploy operator, later
dev = optional future developer account
```

---

## Why simplify?

Most real daily work happens as `pl`:

```text
downloads from ChatGPT
unzips packages
runs PyCharm
creates venv
runs uvicorn
uses Git
edits README/docs
```

If `/opt/projects/motorweb` is owned by `dev`, then `pl` constantly hits permission problems.

So the better laptop model is:

```text
pl owns active source repos
developers group allows future dev access
ted is kept out of source repos
```

---

## Recommended ownership

```text
/opt/projects
owner: pl
group: developers
mode: 2775

/opt/projects/motorweb
owner: pl
group: developers
mode: 2775
```

Expected:

```bash
ls -ld /opt/projects
ls -ld /opt/projects/motorweb
```

Example:

```text
drwxrwsr-x pl developers /opt/projects
drwxrwsr-x pl developers /opt/projects/motorweb
```

---

## User roles

### pl

```text
primary developer
GitHub user
PyCharm user
downloads and unzips files
runs venv
runs tests
commits and pushes code
sudo/admin
```

### dev

```text
optional future developer
not required right now
can be created later
can be added to developers group later
```

### ted

```text
test/deploy operator
no source repo write
deploys tagged releases later
uses /opt/releases and /opt/envs
```

---

## Group model

Keep the `developers` group.

```text
pl  → developers
dev → developers later if needed
ted → not developers
```

Check:

```bash
id pl
id ted
```

---

## Recommended folder model

```text
/opt/projects/motorweb       # active source repo, owned by pl:developers
/opt/releases/motorweb       # tagged releases, later ted/deployers
/opt/envs/dev/motorweb       # dev runtime
/opt/envs/test/motorweb      # test runtime
/opt/envs/prod/motorweb      # prod runtime
```

---

## Do you need `dev` now?

No.

Do not delete it unless you want to clean up. It can remain unused.

If you want a cleaner laptop setup, you may leave `dev` disabled/unused for now.

---

## Do you need to delete `/opt/projects`?

No, not necessarily.

You can simply change ownership:

```bash
sudo chown -R pl:developers /opt/projects
sudo chmod -R g+rwX /opt/projects
sudo find /opt/projects -type d -exec chmod 2775 {} \;
sudo setfacl -R -m u:pl:rwx,g:developers:rwx /opt/projects
sudo setfacl -R -d -m u:pl:rwx,g:developers:rwx /opt/projects
```

If things are messy, use the reset runbook:

```text
docs/runbooks/reset-opt-projects-to-pl-owned.md
```

---

## Main rule going forward

```text
pl owns active development.
ted owns deploy/test flow later.
service accounts own runtime environments later.
```
