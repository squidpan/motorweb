from app.models import JobPostCreate
from app.repositories.csv_job_repo import CsvJobRepo
from app.repositories.json_job_repo import JsonJobRepo


def test_json_repo_crud(tmp_path):
    repo = JsonJobRepo(tmp_path / "jobs.json")
    created = repo.add_job(
        JobPostCreate(
            post_profile="Python Developer",
            post_desc="Build APIs",
            req_experience=1,
            post_tech_stack=["Python", "FastAPI"],
        )
    )
    assert created.post_id > 0
    assert repo.get_job_by_id(created.post_id).post_profile == "Python Developer"


def test_csv_repo_crud(tmp_path):
    repo = CsvJobRepo(tmp_path / "jobs.csv")
    created = repo.add_job(
        JobPostCreate(
            post_profile="API Tester",
            post_desc="Test REST APIs",
            req_experience=1,
            post_tech_stack=["Postman", "Pytest"],
        )
    )
    assert created.post_id > 0
    assert repo.get_job_by_id(created.post_id).post_tech_stack == ["Postman", "Pytest"]
