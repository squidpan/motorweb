from app.models import JobPost


def seed_jobs() -> list[JobPost]:
    return [
        JobPost(
            post_id=1,
            post_profile="Java Developer",
            post_desc="Must have good experience in core Java and advanced Java",
            req_experience=2,
            post_tech_stack=["Core Java", "J2EE", "Spring Boot", "Hibernate"],
        ),
        JobPost(
            post_id=2,
            post_profile="Frontend Developer",
            post_desc="Experience in building responsive web applications using React",
            req_experience=3,
            post_tech_stack=["HTML", "CSS", "JavaScript", "React"],
        ),
        JobPost(
            post_id=3,
            post_profile="Data Scientist",
            post_desc="Strong background in machine learning and data analysis",
            req_experience=4,
            post_tech_stack=["Python", "Machine Learning", "Data Analysis"],
        ),
        JobPost(
            post_id=4,
            post_profile="Network Engineer",
            post_desc="Design and implement computer networks for efficient data communication",
            req_experience=5,
            post_tech_stack=["Networking", "Cisco", "Routing", "Switching"],
        ),
        JobPost(
            post_id=5,
            post_profile="Mobile App Developer",
            post_desc="Experience in mobile app development for iOS and Android",
            req_experience=3,
            post_tech_stack=["iOS Development", "Android Development", "Mobile App"],
        ),
    ]
