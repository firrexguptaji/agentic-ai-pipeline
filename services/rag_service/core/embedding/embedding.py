import google.generativeai as genai

from shared.config.settings import settings
from shared.logging.logger import get_logger

logger = get_logger("rag-service")


class EmbeddingService:
    """
    Generates vector embeddings using the Gemini Embedding API.
    """

    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = settings.EMBEDDING_MODEL

    def embed(self, text: str) -> list[float]:
        """
        Generate an embedding for the supplied text.
        """

        try:
            result = genai.embed_content(
                model=self.model,
                content=text,
            )

            embedding = result["embedding"]

            logger.debug(
                "Generated embedding (%d dimensions)",
                len(embedding),
            )

            return embedding

        except Exception as e:
            logger.exception(
                "Failed to generate embedding."
            )
            raise ValueError(
                f"Embedding generation error: {str(e)}"
            )