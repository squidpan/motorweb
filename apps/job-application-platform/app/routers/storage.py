from fastapi import APIRouter

from app.config import settings

router = APIRouter(prefix="/storage", tags=["storage"])


@router.get("")
def get_storage_info():
    return {
        "active_backend": settings.storage_backend,
        "json_data_file": str(settings.json_data_file),
        "csv_data_file": str(settings.csv_data_file),
        "supported_backends": ["json", "csv"],
        "planned_backends": ["sqlite", "postgres"],
        "data_model": "job_application_platform_flat_file_v1",
    }
