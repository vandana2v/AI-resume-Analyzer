from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from app.database import users_collection, resumes_collection
from app.auth import hash_password, verify_password, create_access_token
from app.resume_parser import extract_text
from app.job_matcher import match_jobs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserAuth(BaseModel):
    username: str
    password: str


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer Backend Running"}


@app.post("/register")
def register(user: UserAuth):
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    users_collection.insert_one({
        "username": user.username,
        "password": hash_password(user.password)
    })

    return {"message": "User registered successfully"}


@app.post("/login")
def login(user: UserAuth):
    existing_user = users_collection.find_one({"username": user.username})

    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }


@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        resume_text = extract_text(file.file)

        resumes_collection.insert_one({
            "filename": file.filename,
            "resume_text": resume_text
        })

        jobs = match_jobs(resume_text)

        return {
            "message": "Resume analyzed successfully",
            "jobs": jobs
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))