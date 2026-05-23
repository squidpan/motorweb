# Runbook - Validate Local Development Environment

Use this after setting up or changing the workstation.

---

## 1. Validate OS

```bash
cat /etc/os-release
uname -a
```

---

## 2. Validate Python

```bash
python3 --version
python3.13 --version
```

---

## 3. Validate Git and SSH

```bash
git --version
ssh -V
ssh -T github-squidpan
```

Expected GitHub SSH success:

```text
Hi squidpan! You've successfully authenticated...
```

---

## 4. Validate repo location

```bash
cd /opt/projects/motorweb
git status
git remote -v
```

Expected remote:

```text
git@github-squidpan:squidpan/motorweb.git
```

---

## 5. Validate permissions

```bash
ls -ld /opt/projects
ls -ld /opt/projects/motorweb
id
```

Expected ownership pattern:

```text
pl developers
```

for simplified laptop model.

---

## 6. Validate venv

```bash
cd /opt/projects/motorweb/apps/job-application-platform
rm -rf .venv
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 7. Validate FastAPI app

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## 8. Validate curl

In another terminal:

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/jobs
curl http://127.0.0.1:8000/storage
```

---

## 9. Validate optional tools

```bash
docker --version
kubectl version --client
helm version
node --version
npm --version
java -version
```

It is okay if `kind` is not installed yet.

---

## 10. Expected Current Gaps

Based on captured reference output:

```text
global pip command not found
kind not installed
Postman not installed
```

These are acceptable right now.

Use `.venv` and `python -m pip`.

Use Insomnia, Swagger, and curl for API testing.

Install `kind` later when local Kubernetes work begins.
