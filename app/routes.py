"""
API routes for profiles, matching, and mentorship
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Student, Mentor
from app.schemas import StudentCreate, StudentResponse, MentorCreate, MentorResponse
from app.auth import hash_password, create_access_token

router = APIRouter(prefix="/api", tags=["profiles"])

# ============ Student Routes ============

@router.post("/students/profile", response_model=StudentResponse)
async def create_student_profile(
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    """Create student profile"""
    # Check if user exists
    user_id = 1  # TODO: Get from JWT token
    
    # Create student record
    db_student = Student(
        user_id=user_id,
        full_name=student_data.full_name,
        field_of_study=student_data.field_of_study,
        year=student_data.year,
        bio=student_data.bio,
        interested_fields=student_data.interested_fields,
        career_goals=student_data.career_goals
    )
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    
    return db_student

@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_student_profile(
    student_id: int,
    db: Session = Depends(get_db)
):
    """Get student profile by ID"""
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return student

# ============ Mentor Routes ============

@router.post("/mentors/profile", response_model=MentorResponse)
async def create_mentor_profile(
    mentor_data: MentorCreate,
    db: Session = Depends(get_db)
):
    """Create mentor profile"""
    # Check if user exists
    user_id = 1  # TODO: Get from JWT token
    
    # Create mentor record
    db_mentor = Mentor(
        user_id=user_id,
        full_name=mentor_data.full_name,
        company=mentor_data.company,
        job_title=mentor_data.job_title,
        years_experience=mentor_data.years_experience,
        bio=mentor_data.bio,
        areas_of_expertise=mentor_data.areas_of_expertise
    )
    
    db.add(db_mentor)
    db.commit()
    db.refresh(db_mentor)
    
    return db_mentor

@router.get("/mentors/{mentor_id}", response_model=MentorResponse)
async def get_mentor_profile(
    mentor_id: int,
    db: Session = Depends(get_db)
):
    """Get mentor profile by ID"""
    mentor = db.query(Mentor).filter(Mentor.id == mentor_id).first()
    
    if not mentor:
        raise HTTPException(status_code=404, detail="Mentor not found")
    
    return mentor