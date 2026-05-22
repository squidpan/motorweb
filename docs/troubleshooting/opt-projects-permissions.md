# `/opt/projects` Permissions Troubleshooting

## Correct `/opt/projects` permission

Expected:

```bash
ls -ld /opt/projects
```

```text
drwxrwsr-x dev developers ... /opt/projects
```

This is correct.

## Confirm current user groups

```bash
id
```

For `pl`, expected to include:

```text
developers
sudo
env-dev
env-test
env-prod
```

## Test whether `pl` can write to `/opt/projects`

```bash
cd /opt/projects
touch pl-write-test.txt
ls -l pl-write-test.txt
rm pl-write-test.txt
```

Expected file owner/group may be:

```text
pl developers
```

That is fine.

## If `pl` cannot write

```bash
ls -ld /opt/projects
id
```

Repair:

```bash
sudo chown dev:developers /opt/projects
sudo chmod 2775 /opt/projects
sudo setfacl -m g:developers:rwx /opt/projects
sudo setfacl -d -m g:developers:rwx /opt/projects
```

If `pl` was recently added to `developers`, refresh current shell:

```bash
newgrp developers
```

or log out and log back in.

## Correct `/opt/projects/motorweb` permission

Expected:

```bash
ls -ld /opt/projects/motorweb
```

```text
drwxrwsr-x dev developers ... /opt/projects/motorweb
```

Repair:

```bash
sudo chown -R dev:developers /opt/projects/motorweb
sudo chmod -R g+rwX /opt/projects/motorweb
sudo find /opt/projects/motorweb -type d -exec chmod 2775 {} \\;
sudo setfacl -R -m g:developers:rwx /opt/projects/motorweb
sudo setfacl -R -d -m g:developers:rwx /opt/projects/motorweb
```

## Git add fails with index.lock permission denied

Symptom:

```text
fatal: Unable to create '/opt/projects/motorweb/.git/index.lock': Permission denied
```

Likely cause: current shell has not picked up the `developers` group yet.

Fix:

```bash
newgrp developers
cd /opt/projects/motorweb
git add .
```

Permanent fix: log out and log back in.

## Git dubious ownership

Symptom:

```text
fatal: detected dubious ownership in repository at '/opt/projects/motorweb'
```

Fix:

```bash
git config --global --add safe.directory /opt/projects/motorweb
```

## Do not use sudo for Git

Avoid:

```bash
sudo git add .
sudo git commit
sudo git push
```

It can create root-owned files inside `.git` and break normal development permissions.
