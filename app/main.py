"""
MentorBridge API - Phase 0
Handles user authentication and basic endpoints
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.database import engine, Base
from app.models import User, Student, Mentor, MentorshipSession
from app.auth import create_access_token, hash_password
from app.routes import router

# Create database tables on startup
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="MentorBridge API",
    description="Connecting students to working professionals",
    version="0.1.0"
)

# ============ Data Models ============

class SignupRequest(BaseModel):
    """User signup request body"""
    email: str
    password: str
    role: str  # "student" or "mentor"

class LoginRequest(BaseModel):
    """User login request body"""
    email: str
    password: str

# ============ Routes ============
# Include routers
app.include_router(router)

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "mentorbridge-backend"}

@app.post("/auth/signup")
async def signup(request: SignupRequest):
    """User signup endpoint with password hashing"""
    if request.role not in ["student", "mentor"]:
        raise HTTPException(status_code=400, detail="Role must be 'student' or 'mentor'")
    
    # Hash password
    hashed_pwd = hash_password(request.password)
    
    # Create token
    access_token = create_access_token(data={"sub": request.email})
    
    return {
        "message": "Signup successful",
        "email": request.email,
        "role": request.role,
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.post("/auth/login")
async def login(request: LoginRequest):
    """User login endpoint"""
    return {
        "message": "Login successful",
        "email": request.email,
        "token": "placeholder_jwt_token"
    }