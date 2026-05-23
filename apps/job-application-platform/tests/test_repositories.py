from app.models import JobPostCreate, JobPostUpdate
from app.repositories.csv_job_repo import CsvJobRepo
from app.repositories.json_job_repo import JsonJobRepo


def make_job(position: str = "Python Developer") -> JobPostCreate:
    return JobPostCreate(
        job_position=position,
        company="Motorweb Labs",
        max_salary=100000,
        location="Remote",
        status="Bookmarked",
        date_saved="05/22/2026",
        source="pytest",
        notes="Created by repository test",
    )


def test_json_repo_crud(tmp_path):
    repo = JsonJobRepo(tmp_path / "jobs.json")
    created = repo.add_job(make_job())
    assert created.post_id >= 1
    assert created.job_position == "Python Developer"

    updated = repo.update_job(created.post_id, JobPostUpdate(status="Applied"))
    assert updated is not None
    assert updated.status == "Applied"

    assert repo.delete_job(created.post_id) is True


def test_csv_repo_crud(tmp_path):
    repo = CsvJobRepo(tmp_path / "jobs.csv")
    created = repo.add_job(make_job("API Tester"))
    assert created.job_position == "API Tester"

    fetched = repo.get_job_by_id(created.post_id)
    assert fetched is not None
    assert fetched.company == "Motorweb Labs"

    assert repo.delete_job(created.post_id) is True
