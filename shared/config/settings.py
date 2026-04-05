from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # -----------------------
    # Environment
    # -----------------------
    ENV: str = "dev"

    # -----------------------
    # API Gateway
    # -----------------------
    AGENT_SERVICE_URL: str = "http://localhost:8001/generate"
    RAG_SERVICE_URL: str = "http://localhost:8002"
    REQUEST_TIMEOUT: int = 15

    # -----------------------
    # LLM
    # -----------------------
    GEMINI_API_KEY: str
    MODEL_NAME: str = "gemini-2.5-flash"

    # -----------------------
    # Embedding
    # -----------------------
    EMBEDDING_MODEL: str = "models/gemini-embedding-001"

    # -----------------------
    # Vector DB
    # -----------------------
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "documents"
    VECTOR_SIZE: int = 3072

    # -----------------------
    # RAG CONFIG (🔥 NEW)
    # -----------------------
    RETRIEVAL_TOP_K: int = 5      # broad search
    FINAL_TOP_K: int = 2          # context for LLM
    SCORE_THRESHOLD: float = 0.7
    MAX_SOURCES: int = 2

    # -----------------------
    # PROMPT
    # -----------------------
    SYSTEM_PROMPT: str = """You are a precise assistant.

Answer ONLY using the context below.
If the answer is not in the context, say "I don't know".

Keep answer concise (1-2 lines).
"""

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()