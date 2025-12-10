# Dashboard Backend API

FastAPI service for the Enterprise Dashboard.

Quick start (local):
- Ensure Python 3.10+ and a virtual environment.
- Install dependencies: `pip install -r requirements.txt`
- Run the server: `python -m src.api.main`

Environment variables (set via .env by orchestrator):
- REACT_APP_PORT: Port to bind the FastAPI app (default: 3001)
- REACT_APP_HEALTHCHECK_PATH: Health endpoint path (default: /healthz)

Health endpoints:
- GET /           -> {"status":"ok"}
- GET /healthz    -> {"status":"healthy"} (or custom path via REACT_APP_HEALTHCHECK_PATH)
