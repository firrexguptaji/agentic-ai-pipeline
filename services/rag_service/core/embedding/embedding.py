import os
from dotenv import load_dotenv
import google.generativeai as genai

from shared.config.settings import settings
from shared.logging.logger import get_logger

load_dotenv()
logger = get_logger("rag-service")

class EmbeddingService:
    def __init__(self):

        genai.configure(api_key=settings.GEMINI_API_KEY)

        # ✅ Use embedding model
        self.model = settings.EMBEDDING_MODEL

    def embed(self, text: str):
        try:
            result = genai.embed_content(
                model=self.model,
                content=text
            )

            return result["embedding"]

        except Exception as e:
            logger.exception("Embedding generation failed")
            raise ValueError(f"Embedding generation error: {str(e)}")