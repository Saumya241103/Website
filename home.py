from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory=Path(__file__).resolve().parent)


@router.get("/", response_class=HTMLResponse)
def home(request: Request):

    skills = [
        "Python",
        "FastAPI",
        "Data Analysis",
        "MySQL",
        "Automations",
        "Computer Vision",
        "Networking"
    ]

    experiences = [
        {
            "role": "Python Developer",
            "company": "Ketsol Private Limited",
            "period": "22 June 2026 - Present",
            "description": "Building automation scripts, backend APIs, and data workflows with Python, FastAPI, and SQL.",
            "highlights": ["API development", "Data analysis", "Automation"]
        },
        {
            "role": "Python Developer Intern",
            "company": "Ketsol Private Limited",
            "period": "17 January 2025 - September 2025",
            "description": "Internship focused on developing automation scripts, backend APIs, and data workflows using Python, FastAPI, and SQL.",
            "highlights": ["API development", "Data analysis", "Automation"]
        },
        {
            "role": "Project Developer",
            "company": "SSIP 2.0",
            "period": "2024",
            "description": "Worked on a vehicle location and accident/fire detection system using Arduino-based hardware and practical system design.",
            "highlights": ["Arduino UNO", "IoT prototype", "Problem solving"]
        },
        {
            "role": "Python Project Developed \"Whatsapp Automated Messaging System\"",
            "company": "Personal Project",
            "period": "2024",
            "description": "Developed a Whatsapp automated messaging system to for an status update .",
            "highlights": ["Python", "Selenium", "Automation"]
        }
    ]

    return templates.TemplateResponse(
        request,
        "home.html",
        {
            "skills": skills,
            "experiences": experiences
        }
    )
