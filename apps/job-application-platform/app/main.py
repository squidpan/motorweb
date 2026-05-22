from fastapi import FastAPI

from app.routers.jobs import router as jobs_router
from app.routers.storage import router as storage_router

app = FastAPI(
    title="JobApp Python API",
    description="FastAPI version of the Java Spring Boot MVC JobApp project.",
    version="0.2.0",
)


@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}


@app.get("/version", tags=["system"])
def version():
    return {"name": "jobapp-py", "version": "0.2.0"}


app.include_router(jobs_router)
app.include_router(storage_router)
