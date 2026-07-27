# MentorBridge Backend

FastAPI server connecting students to working professionals for real-time career guidance.

## Phase 0: Authentication & API Setup

**Status:** In Progress  
**Goal:** Core FastAPI structure + JWT auth ready

**Features:**
- Signup/Login endpoints
- User role support (student/mentor)
- Interactive API docs (Swagger UI)
- Error handling

## Tech Stack

- **Framework:** FastAPI
- **Server:** Uvicorn
- **Database:** PostgreSQL (upcoming)
- **Auth:** JWT (upcoming)
- **AI:** Claude API (upcoming)

## Getting Started

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload

# Visit interactive docs
# http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | API info |
| GET | `/health` | Health check |
| POST | `/auth/signup` | User registration |
| POST | `/auth/login` | User login |

## Next Steps (Phase 1)

- [ ] Add PostgreSQL database connection
- [ ] Implement real JWT tokens
- [ ] Add student/mentor profile models
- [ ] Basic matching algorithm

## Author

Nikitha Kantha | AI & CS Year 2 | St. Ann's College for Women