# curl Test Examples

Run from:

```bash
cd apps/job-application-platform
uvicorn app.main:app --reload
```

## Health

```bash
curl http://127.0.0.1:8000/health
```

## Storage Backend

```bash
curl http://127.0.0.1:8000/storage
```

## Get Jobs

```bash
curl http://127.0.0.1:8000/jobs
```

## Create Job

```bash
curl -X POST http://127.0.0.1:8000/jobs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Python API Developer",
    "company": "Modern Platform Labs",
    "location": "Remote",
    "description": "Build FastAPI services",
    "salary": "100000"
  }'
```
