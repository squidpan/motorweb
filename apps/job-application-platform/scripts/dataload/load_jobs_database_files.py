#!/usr/bin/env python3
"""Load processed dataload files into the active flat-file database folder.

This script copies/creates:
    data/database-files/jobs/jobs.json
    data/database-files/jobs/jobs.csv

It does not call the API. It prepares the file-backed database used by the app.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from datetime import datetime
from pathlib import Path

FIELDNAMES = [
    "post_id",
    "job_position",
    "company",
    "max_salary",
    "location",
    "status",
    "date_saved",
    "source",
    "notes",
]


def backup_if_exists(path: Path, archive_dir: Path) -> None:
    if path.exists():
        archive_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(path, archive_dir / f"{path.stem}-{stamp}{path.suffix}")


def write_csv(jobs: list[dict], output_csv: Path) -> None:
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for job in jobs:
            writer.writerow({name: job.get(name, "") for name in FIELDNAMES})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", type=Path, default=Path("data/dataload/processed/dataload-jobs.json"))
    parser.add_argument("--db-json", type=Path, default=Path("data/database-files/jobs/jobs.json"))
    parser.add_argument("--db-csv", type=Path, default=Path("data/database-files/jobs/jobs.csv"))
    parser.add_argument("--archive-dir", type=Path, default=Path("data/database-files/archive"))
    parser.add_argument("--no-backup", action="store_true")
    args = parser.parse_args()

    jobs = json.loads(args.input_json.read_text(encoding="utf-8"))

    if not args.no_backup:
        backup_if_exists(args.db_json, args.archive_dir)
        backup_if_exists(args.db_csv, args.archive_dir)

    args.db_json.parent.mkdir(parents=True, exist_ok=True)
    args.db_json.write_text(json.dumps(jobs, indent=2, ensure_ascii=False), encoding="utf-8")
    write_csv(jobs, args.db_csv)
    print(f"Loaded {len(jobs)} jobs into {args.db_json} and {args.db_csv}")


if __name__ == "__main__":
    main()
