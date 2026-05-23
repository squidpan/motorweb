# Runbook - Kill Stale Uvicorn Process

Use this when FastAPI cannot start because port `8000` is already in use.

---

## 1. Confirm the error

Typical error:

```text
[Errno 98] Address already in use
```

---

## 2. Check port 8000

```bash
ss -tulpen | grep 8000
```

If output appears, something is listening on port `8000`.

---

## 3. Identify the process

```bash
sudo lsof -nP -iTCP:8000 -sTCP:LISTEN
```

Example:

```text
COMMAND     PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
uvicorn   47300   pl    3u  IPv4 718391      0t0  TCP 127.0.0.1:8000 (LISTEN)
python3.1 52622   pl    3u  IPv4 718391      0t0  TCP 127.0.0.1:8000 (LISTEN)
```

---

## 4. Kill the process

Graceful:

```bash
kill 47300 52622
```

Force only if needed:

```bash
kill -9 47300 52622
```

Alternative:

```bash
pkill -f uvicorn
```

---

## 5. Confirm port is free

```bash
ss -tulpen | grep 8000
```

Expected:

```text
no output
```

---

## 6. Restart API

```bash
cd /opt/projects/motorweb/apps/job-application-platform
source .venv/bin/activate
uvicorn app.main:app --reload
```

---

## 7. Fallback: run on another port

```bash
uvicorn app.main:app --reload --port 8001
```

Open:

```text
http://127.0.0.1:8001/docs
```
