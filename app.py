"""Main entry point for deployment platforms."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from api.main import app  # noqa: E402

# This is the ASGI application that deployment platforms will use
# Usage: uvicorn app:app --host 0.0.0.0 --port $PORT
