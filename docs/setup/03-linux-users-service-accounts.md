# 03 - Linux Users, Groups, Service Accounts, and Environment Access

Goal: create a realistic local multi-user engineering model.

Human users:

```text
pl   = admin/sudo user
dev  = developer/test user
ted  = test/deploy operator
```

Service accounts:

```text
svc-dev
svc-test
svc-prod
```

Groups:

```text
developers
deployers
env-dev
env-test
env-prod
```

---

## 1. Create human users

Do this from `pl`.

```bash
sudo adduser dev
sudo adduser ted
```

---

## 2. Create service accounts

These are not normal human login accounts.

```bash
sudo adduser --system --group svc-dev
sudo adduser --system --group svc-test
sudo adduser --system --group svc-prod
```

---

## 3. Create groups

```bash
sudo groupadd developers
sudo groupadd deployers
sudo groupadd env-dev
sudo groupadd env-test
sudo groupadd env-prod
```

If a group already exists, check with:

```bash
getent group developers
```

---

## 4. Add users to groups

```bash
sudo usermod -aG developers pl
sudo usermod -aG developers dev

sudo usermod -aG deployers ted

sudo usermod -aG env-dev pl
sudo usermod -aG env-test pl
sudo usermod -aG env-prod pl

sudo usermod -aG env-dev dev

sudo usermod -aG env-test ted
sudo usermod -aG env-prod ted
```

Important:

```text
ted has test/prod deploy access but does not have developers group access.
```

---

## 5. Apply new group membership

Best option: log out and log back in.

Check:

```bash
id pl
id dev
id ted
```

---

## 6. Create folders

```bash
sudo mkdir -p /opt/projects
sudo mkdir -p /opt/releases/motorweb
sudo mkdir -p /opt/envs/dev/motorweb
sudo mkdir -p /opt/envs/test/motorweb
sudo mkdir -p /opt/envs/prod/motorweb
```

---

## 7. Set ownership

```bash
sudo chown -R dev:developers /opt/projects
sudo chown -R ted:deployers /opt/releases
sudo chown -R svc-dev:env-dev /opt/envs/dev
sudo chown -R svc-test:env-test /opt/envs/test
sudo chown -R svc-prod:env-prod /opt/envs/prod
```

---

## 8. Set permissions

```bash
sudo chmod -R 2775 /opt/projects
sudo chmod -R 2775 /opt/releases
sudo chmod -R 2775 /opt/envs/dev
sudo chmod -R 2775 /opt/envs/test
sudo chmod -R 2770 /opt/envs/prod
```

The `2` sets the setgid bit so new files inherit the directory group.

---

## 9. Move or clone source repo

Recommended source repo location:

```text
/opt/projects/motorweb
```

Example:

```bash
sudo cp -a ~/pjs/repos/PycharmProjects/motorweb /opt/projects/
sudo chown -R dev:developers /opt/projects/motorweb
sudo chmod -R 2775 /opt/projects/motorweb
```

---

## 10. Deployment pattern

As `dev`:

```bash
git tag v0.1.0
git push origin v0.1.0
```

As `ted`:

```bash
cd /opt/releases/motorweb
git clone --branch v0.1.0 git@github-squidpan:squidpan/motorweb.git v0.1.0
```

Deploy to test:

```bash
cp -a /opt/releases/motorweb/v0.1.0/* /opt/envs/test/motorweb/
```

Deploy to prod:

```bash
cp -a /opt/releases/motorweb/v0.1.0/* /opt/envs/prod/motorweb/
```

---

## 11. Configurable prod access

Give ted prod access:

```bash
sudo usermod -aG env-prod ted
```

Remove ted prod access:

```bash
sudo gpasswd -d ted env-prod
```

Check:

```bash
id ted
```
