from app.config import settings
from app.repositories.base import JobRepository
from app.repositories.csv_job_repo import CsvJobRepo
from app.repositories.json_job_repo import JsonJobRepo


def build_job_repo() -> JobRepository:
    """Create the configured repository implementation."""

    if settings.storage_backend == "json":
        return JsonJobRepo(settings.json_data_file)

    if settings.storage_backend == "csv":
        return CsvJobRepo(settings.csv_data_file)

    raise ValueError(
        f"Unsupported JOBAPP_STORAGE_BACKEND={settings.storage_backend!r}. "
        "Use 'json' or 'csv'. Later we can add 'postgres'."
    )
