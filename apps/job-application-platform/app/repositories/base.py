from abc import ABC, abstractmethod

from app.models import JobPost, JobPostCreate, JobPostUpdate


class JobRepository(ABC):
    """Repository contract.

    The service layer depends on this interface, not on JSON, CSV, or a database
    directly. Later, a PostgresJobRepo can implement this same contract.
    """

    @abstractmethod
    def get_all_jobs(self) -> list[JobPost]:
        raise NotImplementedError

    @abstractmethod
    def get_job_by_id(self, post_id: int) -> JobPost | None:
        raise NotImplementedError

    @abstractmethod
    def add_job(self, job_create: JobPostCreate) -> JobPost:
        raise NotImplementedError

    @abstractmethod
    def update_job(self, post_id: int, job_update: JobPostUpdate) -> JobPost | None:
        raise NotImplementedError

    @abstractmethod
    def delete_job(self, post_id: int) -> bool:
        raise NotImplementedError
