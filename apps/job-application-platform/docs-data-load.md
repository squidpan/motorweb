# JobApp Data Load Quick Notes

Run from this folder:

```bash
cd /opt/projects/motorweb/apps/job-application-platform
source .venv/bin/activate
scripts/dataload/run-initial-dataload.sh
```

Then run the API against JSON database files:

```bash
scripts/run-json.sh
```

Test:

```bash
curl http://127.0.0.1:8000/jobs
curl 'http://127.0.0.1:8000/jobs?status=Applied'
curl 'http://127.0.0.1:8000/jobs?keyword=Analyst'
```
