from pydantic import BaseModel, Field


class JobPostBase(BaseModel):
    post_profile: str = Field(..., examples=["Python Developer"])
    post_desc: str = Field(..., examples=["Build and support REST APIs using Python and FastAPI"])
    req_experience: int = Field(..., ge=0, examples=[2])
    post_tech_stack: list[str] = Field(default_factory=list, examples=[["Python", "FastAPI", "PostgreSQL"]])


class JobPostCreate(JobPostBase):
    pass


class JobPostUpdate(BaseModel):
    post_profile: str | None = None
    post_desc: str | None = None
    req_experience: int | None = Field(default=None, ge=0)
    post_tech_stack: list[str] | None = None


class JobPost(JobPostBase):
    post_id: int
