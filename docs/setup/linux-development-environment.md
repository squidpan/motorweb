# Linux Development Environment Setup

This document describes how to prepare a Linux workstation for `motorweb`.

---

## 1. Base Packages

On Pop!_OS / Ubuntu-based systems:

```bash
sudo apt update
sudo apt install -y git curl zip unzip openssh-client
```

---

## 2. Python 3.13

Confirm:

```bash
python3.13 --version
```

Expected example:

```text
Python 3.13.13
```

If `python3.13` is missing, install Python 3.13 using your preferred trusted method for Pop!_OS/Ubuntu.

Also confirm venv support:

```bash
python3.13 -m venv --help
```

If missing:

```bash
sudo apt install python3.13-venv
```

---

## 3. Project Virtual Environment

From the app folder:

```bash
cd /opt/projects/motorweb/apps/job-application-platform
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Do not rely on global `pip`.

Use:

```bash
python -m pip
```

inside `.venv`.

---

## 4. Run the App

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

If port 8000 is busy:

```bash
uvicorn app.main:app --reload --port 8001
```

---

## 5. Recommended Working Location

```text
/opt/projects/motorweb
```

Current simplified laptop model:

```text
pl owns active development
ted handles deploy/test later
dev is optional/future
```

Recommended ownership:

```bash
sudo chown -R pl:developers /opt/projects
sudo chmod -R g+rwX /opt/projects
sudo find /opt/projects -type d -exec chmod 2775 {} \;
```

---

## 6. Optional Tools

Recommended later:

```text
Docker
kubectl
Helm
kind or k3d
PyCharm
Obsidian
Insomnia or Postman
Node.js/npm
Java
```

These are not required for the first FastAPI run, but will matter for the full platform roadmap.
