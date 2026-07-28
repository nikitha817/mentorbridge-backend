"""
MentorBridge API - Phase 0
Handles user authentication and basic endpoints
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

@app.get("/")
async def root():
    """API root endpoint - returns service info"""
    return {"message": "MentorBridge API v0.1"}

# ... rest of code