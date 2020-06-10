import os
from .message import bot

# Shared logging import for both client and default.py (for headless)
RSENG_LOG_LEVEL = os.environ.get("RSENG_LOG_LEVEL", "INFO")
RSENG_LOG_LEVELS = ["DEBUG", "CRITICAL", "ERROR", "WARNING", "INFO", "QUIET", "FATAL"]
if RSENG_LOG_LEVEL not in RSENG_LOG_LEVELS:
    RSENG_LOG_LEVEL = "INFO"
