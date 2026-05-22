from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_jobs():
    response = client.get("/jobs")
    assert response.status_code == 200
    assert len(response.json()) >= 5


def test_create_job():
    payload = {
        "post_profile": "Python API Developer",
        "post_desc": "Build REST APIs with FastAPI",
        "req_experience": 1,
        "post_tech_stack": ["Python", "FastAPI", "Docker"],
    }
    response = client.post("/jobs", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["post_profile"] == "Python API Developer"
    assert "post_id" in data
