#!/usr/bin/env python3
"""Convert a Teal/exported jobs CSV into motorweb JSON format.

Input columns:
    job_position, company, max_salary, location, status, date_saved

Output records:
    post_id, job_position, company, max_salary, location, status, date_saved, source, notes
"""

from __future__ import annotations

import argparse
import csv
import json
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


def parse_salary(value: str | None) -> int:
    if not value:
        return 0
    cleaned = value.replace("$", "").replace(",", "").strip()
    return int(cleaned or 0)


def convert(input_csv: Path, output_json: Path, source: str = "teal") -> list[dict]:
    jobs: list[dict] = []
    with input_csv.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader, start=1):
            jobs.append(
                {
                    "post_id": index,
                    "job_position": (row.get("job_position") or "").strip(),
                    "company": (row.get("company") or "").strip(),
                    "max_salary": parse_salary(row.get("max_salary")),
                    "location": (row.get("location") or "").strip(),
                    "status": (row.get("status") or "Bookmarked").strip() or "Bookmarked",
                    "date_saved": (row.get("date_saved") or "").strip(),
                    "source": source,
                    "notes": "",
                }
            )
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(jobs, indent=2, ensure_ascii=False), encoding="utf-8")
    return jobs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path, help="Input jobs CSV")
    parser.add_argument("--output", required=True, type=Path, help="Output jobs JSON")
    parser.add_argument("--source", default="teal", help="Source label to add to each job")
    args = parser.parse_args()
    jobs = convert(args.input, args.output, args.source)
    print(f"Converted {len(jobs)} jobs: {args.input} -> {args.output}")


if __name__ == "__main__":
    main()
