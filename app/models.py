"""
SQLAlchemy models for MentorBridge
Defines Student, Mentor, and Session database tables
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    """Base user model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # "student" or "mentor"
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Student(Base):
    """Student profile"""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    # Profile info
    full_name = Column(String)
    bio = Column(Text, nullable=True)
    field_of_study = Column(String)  # e.g., "Computer Science"
    year = Column(Integer)  # 1, 2, 3, 4
    
    # Career info
    interested_fields = Column(String, nullable=True)  # comma-separated
    career_goals = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

class Mentor(Base):
    """Mentor profile"""
    __tablename__ = "mentors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    # Profile info
    full_name = Column(String)
    bio = Column(Text, nullable=True)
    
    # Work info
    company = Column(String)
    job_title = Column(String)
    years_experience = Column(Integer)
    
    # Expertise
    areas_of_expertise = Column(String)  # comma-separated
    willing_to_mentor = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

class MentorshipSession(Base):
    """Mentorship session tracking"""
    __tablename__ = "mentorship_sessions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    mentor_id = Column(Integer, ForeignKey("mentors.id"))
    
    match_score = Column(Integer)  # 0-100 matching percentage
    status = Column(String)  # "active", "completed", "cancelled"
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)