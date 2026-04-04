# shared/config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AGENT_SERVICE_URL: str = os.getenv(
        "AGENT_SERVICE_URL",
        "http://localhost:8001/generate"  # fallback
    )
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", 15))

settings = Settings()