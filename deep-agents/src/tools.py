from datetime import datetime, timezone
from langchain_core.tools import tool

@tool
def get_current_datetime() -> str:
    """Get current date and time in ISO format (UTC)."""
    return datetime.now(timezone.utc).isoformat()