"""FastAPI application for the calculator web UI."""

from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from . import __version__
from .routes import router

# Get the frontend directory path
FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

app = FastAPI(
    title="Calculator API",
    description="A beautiful calculator with REST API",
    version=__version__,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)


@app.get("/")
async def serve_frontend() -> FileResponse:
    """Serve the frontend HTML."""
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/favicon.svg")
async def serve_favicon_svg() -> FileResponse:
    """Serve the SVG favicon."""
    return FileResponse(FRONTEND_DIR / "favicon.svg", media_type="image/svg+xml")


@app.get("/favicon.ico")
async def serve_favicon_ico() -> FileResponse:
    """Serve the favicon (browsers often request .ico)."""
    return FileResponse(FRONTEND_DIR / "favicon.svg", media_type="image/svg+xml")


# Mount static files AFTER explicit routes
app.mount("/css", StaticFiles(directory=FRONTEND_DIR / "css"), name="css")
app.mount("/js", StaticFiles(directory=FRONTEND_DIR / "js"), name="js")


def run() -> None:
    """Run the web server."""
    print("Starting Calculator Web UI at http://localhost:8000")
    print("API docs available at http://localhost:8000/docs")
    print("Press Ctrl+C to stop")
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
