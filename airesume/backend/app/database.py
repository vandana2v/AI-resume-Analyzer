from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)

db = client["ai_resume_analyzer"]

# Collections
users_collection = db["users"]
resumes_collection = db["resumes"]
jobs_collection = db["jobs"]  # optional (only if you store jobs)

# Ensure unique username (important)
users_collection.create_index("username", unique=True)