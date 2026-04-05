import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging
from shared.config.settings import settings

load_dotenv()
logger = logging.getLogger(__name__)

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
            logger.error(f"Embedding error: {str(e)}")
            raise RuntimeError("Embedding generation failed")