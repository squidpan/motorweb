# README Update - v0.4.8 Uvicorn Port Troubleshooting Addendum

Add this under the README troubleshooting quick reference.

---

## Uvicorn Port 8000 Already in Use

If running:

```bash
uvicorn app.main:app --reload
```

fails with:

```text
[Errno 98] Address already in use
```

then another process is already listening on port `8000`.

Quick workaround:

```bash
uvicorn app.main:app --reload --port 8001
```

Better diagnosis:

```bash
ss -tulpen | grep 8000
sudo lsof -nP -iTCP:8000 -sTCP:LISTEN
```

Kill Uvicorn reload processes:

```bash
pkill -f uvicorn
```

or kill specific PIDs:

```bash
kill <PID1> <PID2>
```

See:

```text
docs/troubleshooting/uvicorn-port-conflicts.md
docs/runbooks/kill-stale-uvicorn-process.md
```
