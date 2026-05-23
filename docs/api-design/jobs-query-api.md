# Jobs Query API

The `/jobs` endpoint supports simple file-backed queries.

## Get all jobs

```http
GET /jobs
```

## Filter by status

```http
GET /jobs?status=Applied
GET /jobs?status=Bookmarked
```

## Search by keyword

```http
GET /jobs?keyword=Analyst
```

Keyword checks:

```text
job_position
company
location
status
notes
```

## Filter by company

```http
GET /jobs?company=Citi
```

## Filter by location

```http
GET /jobs?location=New York
```

These are intentionally simple until PostgreSQL search is introduced.
