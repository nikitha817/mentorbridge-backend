# Contributing to MentorBridge

We welcome contributions! Here's how to get started.

## Setup

1. Clone the repository
```bash
   git clone https://github.com/nikitha817/mentorbridge-backend.git
   cd mentorbridge-backend
```

2. Create a virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Create `.env` file (copy from `.env.example`)
```bash
   copy .env.example .env
```

5. Run the server
```bash
   uvicorn app.main:app --reload
```

Visit: http://127.0.0.1:8000/docs

## Making Changes

1. Create a feature branch
```bash
   git checkout -b feature/your-feature-name
```

2. Make your changes and test them

3. Commit with a clear message
```bash
   git add .
   git commit -m "Feature: Clear description of what you changed"
```

4. Push your branch
```bash
   git push origin feature/your-feature-name
```

5. Create a Pull Request on GitHub

## Code Standards

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions
- Keep functions small and focused

## Reporting Issues

- Found a bug? Create an [Issue](https://github.com/nikitha817/mentorbridge-backend/issues)
- Include: what you did, what happened, what you expected
- Add screenshots if helpful

## Questions?

Feel free to open an issue or ask in discussions!

---

**Happy Contributing! 🚀**