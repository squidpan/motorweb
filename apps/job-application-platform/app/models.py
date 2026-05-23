from pydantic import BaseModel, Field


class JobPostBase(BaseModel):
    job_position: str = Field(..., examples=["Production Support Analyst"])
    company: str = Field(..., examples=["Example Company"])
    max_salary: int = Field(default=0, ge=0, examples=[120000])
    location: str = Field(default="", examples=["New York, NY"])
    status: str = Field(default="Bookmarked", examples=["Bookmarked"])
    date_saved: str = Field(default="", examples=["04/24/2026"])
    source: str = Field(default="manual", examples=["teal"])
    notes: str = Field(default="", examples=[""])


class JobPostCreate(JobPostBase):
    pass


class JobPostUpdate(BaseModel):
    job_position: str | None = None
    company: str | None = None
    max_salary: int | None = Field(default=None, ge=0)
    location: str | None = None
    status: str | None = None
    date_saved: str | None = None
    source: str | None = None
    notes: str | None = None


class JobPost(JobPostBase):
    post_id: int
