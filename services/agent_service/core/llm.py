import google.generativeai as genai

from shared.config.settings import settings
from shared.logging.logger import get_logger

logger = get_logger("agent-service")

class LLMProvider:
    def __init__(self):
        api_key = settings.GEMINI_API_KEY or settings.GOOGLE_API_KEY
        
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(settings.MODEL_NAME)

    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)

            if not response or not response.text:
                raise ValueError("Empty response from LLM")

            return response.text

        except Exception as e:
            logger.exception("LLM generation failed")
            raise ValueError(f"LLM generation error: {str(e)}")