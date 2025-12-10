"""Entrypoint module for running the FastAPI app via `uvicorn main:app`.

This file simply exposes the `app` object defined in `src.api.main` so that
commands executed from the repository/container root (e.g., `uvicorn main:app`)
can import and start the service without needing to modify PYTHONPATH.

Usage examples:
- uvicorn main:app --host 0.0.0.0 --port 3001
- python -m uvicorn main:app --host 0.0.0.0 --port 3001
"""

# PUBLIC_INTERFACE
from src.api.main import app  # noqa: F401
