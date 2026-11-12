from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import home
import project as projects

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Saumya Singh - Developer Portfolio",
    description="Personal portfolio and project showcase",
    version="1.0.0"
)

# Static files
app.mount("/static", StaticFiles(directory=BASE_DIR), name="static")

# Routes
app.include_router(home.router)
app.include_router(projects.router)


@app.get("/health")
def health_check():
    return {
        "status": "running",
        "message": "Portfolio API is working"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
