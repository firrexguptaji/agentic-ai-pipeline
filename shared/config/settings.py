import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # -----------------------
    # API Gateway
    # -----------------------
    AGENT_SERVICE_URL: str = os.getenv(
        "AGENT_SERVICE_URL",
        "http://localhost:8001/generate"
    )

    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", 15))

    # -----------------------
    # LLM
    # -----------------------
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    MODEL_NAME: str = os.getenv("MODEL_NAME", "gemini-2.5-flash")

    # -----------------------
    # Embedding
    # -----------------------
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "models/gemini-embedding-001"
    )

    # -----------------------
    # Vector DB (Qdrant)
    # -----------------------
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 6333))
    QDRANT_COLLECTION: str = os.getenv("QDRANT_COLLECTION", "documents")

    # IMPORTANT: update after checking embedding size
    VECTOR_SIZE: int = int(os.getenv("VECTOR_SIZE", 3072))


settings = Settings()