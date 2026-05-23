# Backward-compatible import for older code/tests.
# The old JobRepo name now points to the JSON repository implementation.

from app.config import settings
from app.repositories.json_job_repo import JsonJobRepo


class JobRepo(JsonJobRepo):
    def __init__(self, data_file=None):
        super().__init__(data_file or settings.json_data_file)
