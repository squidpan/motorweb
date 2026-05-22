# Runbook - Reclone `motorweb` Under `/opt/projects`

Use this runbook if the local repo under `/opt/projects/motorweb` has confusing ownership or mixed permissions.

This does not delete SSH keys because SSH keys live under:

```text
/home/pl/.ssh/
```

## 1. Confirm current repo status before deleting

```bash
cd /opt/projects/motorweb
git status
```

If there are uncommitted changes you want to save:

```bash
git diff > ~/motorweb-local-changes.patch
```

## 2. Remove local repo copy

```bash
cd /opt/projects
sudo rm -rf motorweb
```

## 3. Clone from GitHub

```bash
cd /opt/projects
git clone git@github-squidpan:squidpan/motorweb.git
```

## 4. Normalize ownership and permissions

```bash
sudo chown -R dev:developers /opt/projects/motorweb
sudo chmod -R g+rwX /opt/projects/motorweb
sudo find /opt/projects/motorweb -type d -exec chmod 2775 {} \\;
sudo setfacl -R -m g:developers:rwx /opt/projects/motorweb
sudo setfacl -R -d -m g:developers:rwx /opt/projects/motorweb
```

## 5. Mark repo as trusted for `pl`

```bash
git config --global --add safe.directory /opt/projects/motorweb
```

## 6. Validate

```bash
cd /opt/projects/motorweb
git status
touch pl-write-test.txt
git add pl-write-test.txt
git reset pl-write-test.txt
rm pl-write-test.txt
```

Expected: no permission errors.

## 7. Add docs update package on a branch

```bash
cd /opt/projects/motorweb
git checkout -b feature/opt-projects-shared-model
unzip ~/Downloads/motorweb-doc-updates-v0.4.2.zip -d .
git status
git add .
git commit -m "Document shared opt projects model"
git push -u origin feature/opt-projects-shared-model
```

## 8. Merge back to main

```bash
git checkout main
git pull
git merge feature/opt-projects-shared-model
git push origin main
```
