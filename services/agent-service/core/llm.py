import os
from dotenv import load_dotenv
import google.generativeai as genai

# 🔥 THIS LINE IS MISSING (most likely)
load_dotenv()

class LLMProvider:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"