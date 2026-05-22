from functools import lru_cache

from app.repositories.base import JobRepository
from app.repositories.factory import build_job_repo
from app.services.job_service import JobService


@lru_cache
def get_job_repo() -> JobRepository:
    return build_job_repo()


def get_job_service() -> JobService:
    return JobService(get_job_repo())
