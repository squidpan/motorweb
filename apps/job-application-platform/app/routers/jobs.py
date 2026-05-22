from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_job_service
from app.models import JobPost, JobPostCreate, JobPostUpdate
from app.services.job_service import JobService

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("", response_model=list[JobPost])
def get_all_jobs(service: JobService = Depends(get_job_service)):
    return service.get_all_jobs()


@router.get("/{post_id}", response_model=JobPost)
def get_job_by_id(post_id: int, service: JobService = Depends(get_job_service)):
    job = service.get_job_by_id(post_id)
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return job


@router.post("", response_model=JobPost, status_code=status.HTTP_201_CREATED)
def add_job(job_create: JobPostCreate, service: JobService = Depends(get_job_service)):
    return service.add_job(job_create)


@router.put("/{post_id}", response_model=JobPost)
def update_job(post_id: int, job_update: JobPostUpdate, service: JobService = Depends(get_job_service)):
    job = service.update_job(post_id, job_update)
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return job


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(post_id: int, service: JobService = Depends(get_job_service)):
    deleted = service.delete_job(post_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return None
