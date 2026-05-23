from app.models import JobPost, JobPostCreate, JobPostUpdate
from app.repositories.base import JobRepository


class JobService:
    def __init__(self, repository: JobRepository):
        self.repository = repository

    def get_all_jobs(self) -> list[JobPost]:
        return self.repository.get_all_jobs()

    def search_jobs(
        self,
        *,
        status: str | None = None,
        company: str | None = None,
        location: str | None = None,
        keyword: str | None = None,
    ) -> list[JobPost]:
        jobs = self.repository.get_all_jobs()
        if status:
            jobs = [job for job in jobs if job.status.lower() == status.lower()]
        if company:
            jobs = [job for job in jobs if company.lower() in job.company.lower()]
        if location:
            jobs = [job for job in jobs if location.lower() in job.location.lower()]
        if keyword:
            needle = keyword.lower()
            jobs = [
                job for job in jobs
                if needle in job.job_position.lower()
                or needle in job.company.lower()
                or needle in job.location.lower()
                or needle in job.status.lower()
                or needle in job.notes.lower()
            ]
        return jobs

    def get_job_by_id(self, post_id: int) -> JobPost | None:
        return self.repository.get_job_by_id(post_id)

    def add_job(self, job_create: JobPostCreate) -> JobPost:
        return self.repository.add_job(job_create)

    def update_job(self, post_id: int, job_update: JobPostUpdate) -> JobPost | None:
        return self.repository.update_job(post_id, job_update)

    def delete_job(self, post_id: int) -> bool:
        return self.repository.delete_job(post_id)
