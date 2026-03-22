from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Job(BaseModel):
    title: str
    company: str
    skills: str
    description: str

class Resume(BaseModel):
    resume_text: str