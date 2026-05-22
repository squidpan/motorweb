from app.models import JobPost, JobPostCreate, JobPostUpdate
from app.repositories.base import JobRepository


class JobService:
    """Service layer.

    This is the Python version of your Java JobService.
    Business rules will live here later.
    """

    def __init__(self, repo: JobRepository):
        self.repo = repo

    def get_all_jobs(self) -> list[JobPost]:
        return self.repo.get_all_jobs()

    def get_job_by_id(self, post_id: int) -> JobPost | None:
        return self.repo.get_job_by_id(post_id)

    def add_job(self, job_create: JobPostCreate) -> JobPost:
        return self.repo.add_job(job_create)

    def update_job(self, post_id: int, job_update: JobPostUpdate) -> JobPost | None:
        return self.repo.update_job(post_id, job_update)

    def delete_job(self, post_id: int) -> bool:
        return self.repo.delete_job(post_id)
