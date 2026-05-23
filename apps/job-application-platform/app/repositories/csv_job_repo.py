import csv
from pathlib import Path
from threading import Lock

from app.models import JobPost, JobPostCreate, JobPostUpdate
from app.repositories.base import JobRepository
from app.repositories.seed import seed_jobs


class CsvJobRepo(JobRepository):
    """Flat-file repository backed by CSV.

    CSV is useful for Excel/LibreOffice processing. JSON is usually better for
    API loading and scripts. Both backends follow the same repository contract.
    """

    fieldnames = [
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

    def __init__(self, data_file: Path | str):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self._lock = Lock()
        if not self.data_file.exists():
            self._write_jobs(seed_jobs())

    def get_all_jobs(self) -> list[JobPost]:
        return self._read_jobs()

    def get_job_by_id(self, post_id: int) -> JobPost | None:
        return next((job for job in self._read_jobs() if job.post_id == post_id), None)

    def add_job(self, job_create: JobPostCreate) -> JobPost:
        with self._lock:
            jobs = self._read_jobs()
            next_id = max((job.post_id for job in jobs), default=0) + 1
            job = JobPost(post_id=next_id, **job_create.model_dump())
            jobs.append(job)
            self._write_jobs(jobs)
            return job

    def update_job(self, post_id: int, job_update: JobPostUpdate) -> JobPost | None:
        with self._lock:
            jobs = self._read_jobs()
            for index, existing_job in enumerate(jobs):
                if existing_job.post_id == post_id:
                    updated_data = existing_job.model_dump()
                    updated_data.update(job_update.model_dump(exclude_unset=True))
                    updated_job = JobPost(**updated_data)
                    jobs[index] = updated_job
                    self._write_jobs(jobs)
                    return updated_job
            return None

    def delete_job(self, post_id: int) -> bool:
        with self._lock:
            jobs = self._read_jobs()
            new_jobs = [job for job in jobs if job.post_id != post_id]
            if len(new_jobs) == len(jobs):
                return False
            self._write_jobs(new_jobs)
            return True

    def _read_jobs(self) -> list[JobPost]:
        with self.data_file.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            jobs = []
            for row in reader:
                jobs.append(
                    JobPost(
                        post_id=int(row["post_id"]),
                        job_position=row.get("job_position", ""),
                        company=row.get("company", ""),
                        max_salary=int(row.get("max_salary") or 0),
                        location=row.get("location", ""),
                        status=row.get("status", "Bookmarked"),
                        date_saved=row.get("date_saved", ""),
                        source=row.get("source", "csv"),
                        notes=row.get("notes", ""),
                    )
                )
            return jobs

    def _write_jobs(self, jobs: list[JobPost]) -> None:
        with self.data_file.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for job in jobs:
                writer.writerow(job.model_dump())
