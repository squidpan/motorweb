#!/usr/bin/env python3
"""Basic validation for motorweb jobs JSON files without external packages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = ["post_id", "job_position", "company", "max_salary", "location", "status", "date_saved"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", type=Path, default=Path("data/database-files/jobs/jobs.json"))
    args = parser.parse_args()
    jobs = json.loads(args.input_json.read_text(encoding="utf-8"))
    if not isinstance(jobs, list):
        raise SystemExit("ERROR: root JSON value must be a list")
    seen_ids = set()
    for index, job in enumerate(jobs, start=1):
        missing = [field for field in REQUIRED if field not in job]
        if missing:
            raise SystemExit(f"ERROR row {index}: missing fields {missing}")
        if job["post_id"] in seen_ids:
            raise SystemExit(f"ERROR row {index}: duplicate post_id {job['post_id']}")
        seen_ids.add(job["post_id"])
        if not isinstance(job["max_salary"], int):
            raise SystemExit(f"ERROR row {index}: max_salary must be int")
    print(f"Validated {len(jobs)} jobs in {args.input_json}")


if __name__ == "__main__":
    main()
