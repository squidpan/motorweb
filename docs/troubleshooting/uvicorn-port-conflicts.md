# Uvicorn Port Conflicts

This document covers the common FastAPI/Uvicorn error:

```text
[Errno 98] Address already in use
```

---

## Symptom

You run:

```bash
uvicorn app.main:app --reload
```

and see:

```text
ERROR: [Errno 98] Address already in use
```

---

## Meaning

Port `8000` is already being used by another process.

Usually it is:

```text
an old uvicorn process
a uvicorn reload watcher
another Python web server
```

---

## Quick workaround

Run on another port:

```bash
uvicorn app.main:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001/docs
```

---

## Find what is using port 8000

First try:

```bash
ss -tulpen | grep 8000
```

This may show that something is listening on:

```text
127.0.0.1:8000
```

but may not show the process name clearly.

Use `sudo lsof` for better output:

```bash
sudo lsof -nP -iTCP:8000 -sTCP:LISTEN
```

Example output:

```text
COMMAND     PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
uvicorn   47300   pl    3u  IPv4 718391      0t0  TCP 127.0.0.1:8000 (LISTEN)
python3.1 52622   pl    3u  IPv4 718391      0t0  TCP 127.0.0.1:8000 (LISTEN)
```

---

## Why two processes?

When using:

```bash
uvicorn app.main:app --reload
```

Uvicorn may create:

```text
a reload watcher process
a child application process
```

So seeing both:

```text
uvicorn
python3.13
```

or similar is normal.

---

## Kill by PID

If the output shows:

```text
47300
52622
```

kill both:

```bash
kill 47300 52622
```

If they do not stop:

```bash
kill -9 47300 52622
```

---

## Kill all uvicorn processes

If you are sure only your dev server is running:

```bash
pkill -f uvicorn
```

Then check:

```bash
ss -tulpen | grep 8000
```

No output means port `8000` is free.

---

## Use fuser

Another option:

```bash
sudo fuser -v 8000/tcp
```

Kill process using that port:

```bash
sudo fuser -k 8000/tcp
```

---

## Restart

```bash
cd /opt/projects/motorweb/apps/job-application-platform
source .venv/bin/activate
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Prevention

When done testing, stop Uvicorn with:

```text
Ctrl+C
```

inside the terminal where it is running.

If using Tilix split panes/tabs, check for old panes still running Uvicorn.
