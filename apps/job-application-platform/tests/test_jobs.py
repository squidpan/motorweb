from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_get_jobs():
    response = client.get('/jobs')
    assert response.status_code == 200
    jobs = response.json()
    assert isinstance(jobs, list)
    assert len(jobs) >= 1
    assert 'job_position' in jobs[0]


def test_filter_jobs_by_status():
    response = client.get('/jobs?status=Applied')
    assert response.status_code == 200
    for job in response.json():
        assert job['status'] == 'Applied'


def test_create_job():
    payload = {
        'job_position': 'Python API Tester',
        'company': 'Motorweb Labs',
        'max_salary': 100000,
        'location': 'Remote',
        'status': 'Bookmarked',
        'date_saved': '05/22/2026',
        'source': 'pytest',
        'notes': 'Created by test',
    }
    response = client.post('/jobs', json=payload)
    assert response.status_code == 201
    assert response.json()['job_position'] == 'Python API Tester'
