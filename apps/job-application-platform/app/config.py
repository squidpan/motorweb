import os
from pathlib import Path


class Settings:
    """Application settings.

    Flat-file storage is intentionally configurable so the same service/repository
    pattern can later move to PostgreSQL without changing the API contract.

    Examples:
        JOBAPP_STORAGE_BACKEND=json
        JOBAPP_STORAGE_BACKEND=csv
        JOBAPP_JSON_DATA_FILE=data/database-files/jobs/jobs.json
        JOBAPP_CSV_DATA_FILE=data/database-files/jobs/jobs.csv
    """

    storage_backend: str = os.getenv("JOBAPP_STORAGE_BACKEND", "json").lower()
    json_data_file: Path = Path(os.getenv("JOBAPP_JSON_DATA_FILE", "data/database-files/jobs/jobs.json"))
    csv_data_file: Path = Path(os.getenv("JOBAPP_CSV_DATA_FILE", "data/database-files/jobs/jobs.csv"))


settings = Settings()
