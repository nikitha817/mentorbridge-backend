"""
Pydantic schemas for request/response validation
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# ============ Auth Schemas ============

class SignupRequest(BaseModel):
    email: str
    password: str
    role: str  # "student" or "mentor"

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    email: str

# ============ Student Schemas ============

class StudentCreate(BaseModel):
    full_name: str
    field_of_study: str
    year: int
    bio: Optional[str] = None
    interested_fields: Optional[str] = None
    career_goals: Optional[str] = None

class StudentResponse(BaseModel):
    id: int
    full_name: str
    field_of_study: str
    year: int
    bio: Optional[str]
    
    class Config:
        from_attributes = True

# ============ Mentor Schemas ============

class MentorCreate(BaseModel):
    full_name: str
    company: str
    job_title: str
    years_experience: int
    bio: Optional[str] = None
    areas_of_expertise: Optional[str] = None

class MentorResponse(BaseModel):
    id: int
    full_name: str
    company: str
    job_title: str
    years_experience: int
    areas_of_expertise: Optional[str]
    
    class Config:
        from_attributes = True