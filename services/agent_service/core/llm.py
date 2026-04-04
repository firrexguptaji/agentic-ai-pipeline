import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging

load_dotenv()
logger = logging.getLogger(__name__)

class LLMProvider:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)

            if not response or not response.text:
                raise ValueError("Empty response from LLM")

            return response.text

        except Exception as e:
            logger.error(f"LLM error: {str(e)}")
            raise RuntimeError("LLM generation failed")