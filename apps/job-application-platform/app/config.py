import os
from pathlib import Path


class Settings:
    """Application settings.

    For now, the storage backend is selected with an environment variable.

    Examples:
        JOBAPP_STORAGE_BACKEND=json
        JOBAPP_STORAGE_BACKEND=csv
    """

    storage_backend: str = os.getenv("JOBAPP_STORAGE_BACKEND", "json").lower()
    json_data_file: Path = Path(os.getenv("JOBAPP_JSON_DATA_FILE", "app/data/jobs.json"))
    csv_data_file: Path = Path(os.getenv("JOBAPP_CSV_DATA_FILE", "app/data/jobs.csv"))


settings = Settings()
