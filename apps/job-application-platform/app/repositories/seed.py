from app.models import JobPost


def seed_jobs() -> list[JobPost]:
    return [
        JobPost(
            post_id=1,
            job_position="Production Support Analyst",
            company="Example Financial Services",
            max_salary=120000,
            location="New York, NY",
            status="Bookmarked",
            date_saved="04/24/2026",
            source="seed",
            notes="Default seed row created when no flat-file database exists.",
        )
    ]
