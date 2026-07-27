from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="MentorBridge API",
    description="Connecting students to working professionals",
    version="0.1.0"
)

# Data models
class SignupRequest(BaseModel):
    email: str
    password: str
    role: str  # "student" or "mentor"

class LoginRequest(BaseModel):
    email: str
    password: str

# Routes
@app.get("/")
async def root():
    return {"message": "MentorBridge API v0.1"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "mentorbridge-backend"}

@app.post("/auth/signup")
async def signup(request: SignupRequest):
    """User signup endpoint"""
    if request.role not in ["student", "mentor"]:
        raise HTTPException(status_code=400, detail="Role must be 'student' or 'mentor'")
    
    return {
        "message": "Signup successful",
        "email": request.email,
        "role": request.role,
        "status": "user_created"
    }

@app.post("/auth/login")
async def login(request: LoginRequest):
    """User login endpoint"""
    return {
        "message": "Login successful",
        "email": request.email,
        "token": "placeholder_jwt_token"
    }