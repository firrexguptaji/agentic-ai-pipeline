import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging

load_dotenv()
logger = logging.getLogger(__name__)

class EmbeddingService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY")

        genai.configure(api_key=api_key)

        # ✅ Use embedding model
        self.model = "models/gemini-embedding-001"

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