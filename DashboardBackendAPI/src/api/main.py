import os
from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# PUBLIC_INTERFACE
app = FastAPI(
    title="Dashboard Backend API",
    description=(
        "FastAPI-powered backend for the Enterprise Dashboard. "
        "Provides REST APIs and WebSocket interfaces for authentication, "
        "user/team management, dashboards, widgets, analytics, reporting, and notifications."
    ),
    version="1.0.0",
    contact={"name": "Enterprise Dashboard Team", "email": "support@example.com"},
)

# Configure CORS broadly for preview environment; tighten in production via env if needed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this via env configuration.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Determine healthcheck path from environment, defaulting to /healthz
_HEALTH_PATH = os.getenv("REACT_APP_HEALTHCHECK_PATH", "/healthz").strip() or "/healthz"


# PUBLIC_INTERFACE
@app.get(
    "/",
    summary="Service root",
    description="Returns a simple status object to indicate the service is up.",
    tags=["Health"],
    responses={200: {"description": "Service OK"}},
)
def root() -> Dict[str, str]:
    """This route returns a minimal OK payload so that generic root checks succeed."""
    return {"status": "ok"}


# PUBLIC_INTERFACE
@app.get(
    _HEALTH_PATH,
    summary="Health check",
    description="Health probe endpoint used by the preview environment to determine readiness.",
    tags=["Health"],
    responses={
        200: {
            "description": "Service healthy",
            "content": {"application/json": {"example": {"status": "healthy"}}},
        }
    },
)
def health_check() -> JSONResponse:
    """Health check endpoint responding with a 200 and a small JSON payload."""
    return JSONResponse({"status": "healthy"})


# Allow running via `python -m src.api.main` or `python src/api/main.py`
if __name__ == "__main__":
    # Do not hardcode; read from environment with defaults suitable for preview.
    # REACT_APP_PORT is provided by the environment; default to 3001 per task requirement.
    port_str = os.getenv("REACT_APP_PORT", "3001")
    try:
        port = int(port_str)
    except ValueError:
        # Fallback to 3001 if malformed value provided
        port = 3001

    # Bind on all interfaces so the preview/ingress can reach the server.
    import uvicorn

    uvicorn.run(
        "src.api.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        workers=1,
    )
