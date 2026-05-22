# Runbook - Reset `/opt/projects` to pl-owned Laptop Model

Use this when `/opt/projects` or `/opt/projects/motorweb` has confusing ownership from earlier experiments.

This runbook does not affect SSH keys because SSH keys live in:

```text
/home/pl/.ssh/
```

It also does not affect GitHub repositories.

---

## Option A - Keep current repo and repair ownership

Use this if `/opt/projects/motorweb` contains work you want to keep.

### 1. Check repo status first

```bash
cd /opt/projects/motorweb
git status
```

If there are important uncommitted changes, commit them or save a patch:

```bash
git diff > ~/motorweb-local-changes.patch
```

### 2. Repair ownership

```bash
sudo chown -R pl:developers /opt/projects
sudo chmod -R g+rwX /opt/projects
sudo find /opt/projects -type d -exec chmod 2775 {} \;
sudo setfacl -R -m u:pl:rwx,g:developers:rwx /opt/projects
sudo setfacl -R -d -m u:pl:rwx,g:developers:rwx /opt/projects
```

### 3. Refresh shell if needed

```bash
newgrp developers
```

or log out and log back in.

### 4. Validate

```bash
cd /opt/projects/motorweb
touch pl-write-test.txt
rm pl-write-test.txt
cd apps/job-application-platform
rm -rf .venv
python3.13 -m venv .venv
```

---

## Option B - Delete and reclone cleanly

Use this if the local repo is disposable and all important work is already pushed to GitHub.

### 1. Confirm remote is good

```bash
cd /opt/projects/motorweb
git status
git remote -v
```

Expected remote:

```text
git@github-squidpan:squidpan/motorweb.git
```

### 2. Remove local repo copy

```bash
cd /opt/projects
sudo rm -rf motorweb
```

### 3. Make `/opt/projects` pl-owned

```bash
sudo mkdir -p /opt/projects
sudo chown pl:developers /opt/projects
sudo chmod 2775 /opt/projects
sudo setfacl -m u:pl:rwx,g:developers:rwx /opt/projects
sudo setfacl -d -m u:pl:rwx,g:developers:rwx /opt/projects
```

### 4. Clone as pl

```bash
cd /opt/projects
git clone git@github-squidpan:squidpan/motorweb.git
```

### 5. Normalize repo permissions

```bash
sudo chown -R pl:developers /opt/projects/motorweb
sudo chmod -R g+rwX /opt/projects/motorweb
sudo find /opt/projects/motorweb -type d -exec chmod 2775 {} \;
sudo setfacl -R -m u:pl:rwx,g:developers:rwx /opt/projects/motorweb
sudo setfacl -R -d -m u:pl:rwx,g:developers:rwx /opt/projects/motorweb
```

### 6. Validate venv creation

```bash
cd /opt/projects/motorweb/apps/job-application-platform
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Do not use sudo for Git

Avoid:

```bash
sudo git add .
sudo git commit
sudo git push
```

Use `sudo` only for permission repair and system administration.
