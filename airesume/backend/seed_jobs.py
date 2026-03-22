from app.database import jobs_collection

jobs_collection.insert_many([
    {
        "title": "Python Developer",
        "company": "Amazon",
        "skills": "Python, AWS, Docker, FastAPI",
        "description": "Build backend services using Python and AWS"
    },
    {
        "title": "AI Engineer",
        "company": "Google",
        "skills": "Python, Machine Learning, NLP",
        "description": "Develop AI and NLP models"
    },
    {
        "title": "Backend Engineer",
        "company": "Microsoft",
        "skills": "FastAPI, Docker, Cloud",
        "description": "API development and deployment"
    }
])

print("✅ Jobs inserted successfully")