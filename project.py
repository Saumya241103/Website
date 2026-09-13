from fastapi import APIRouter

router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)

projects = [
    {
        "id": 1,
        "name": "NSE Data Visualization and whatsapp integration",
        "technology": ["Python", "NSE API", "Whatsapp API"],
        "description": "Established a data visualization platform for NSE data with integrated WhatsApp notifications."
    },
    {
        "id": 2,
        "name": "Stock Market Alert & Analysis System",
        "technology": ["Python", "MySQL", "Data Analysis", "Whatsapp Automation"],
        "description": "Developed a stock market alert and analysis system with automated WhatsApp notifications."
    }
] 


@router.get("/")
def get_projects():
    return projects


@router.get("/{project_id}")
def get_project(project_id: int):

    for project in projects:
        if project["id"] == project_id:
            return project

    return {
        "error": "Project not found"
    }