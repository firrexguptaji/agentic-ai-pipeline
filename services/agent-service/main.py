from fastapi import FastAPI
from pydantic import BaseModel
import logging
from core.llm import LLMProvider

# -----------------------
# Logging
# -----------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------
# App
# -----------------------
app = FastAPI(title="Agent Service")

llm = LLMProvider()

# -----------------------
# Schema
# -----------------------
class AgentRequest(BaseModel):
    query: str

# -----------------------
# Routes
# -----------------------
@app.get("/")
def health():
    return {"status": "agent running"}

@app.post("/generate")
def generate(request: AgentRequest):
    logger.info(f"Received query: {request.query}")
    response = llm.generate(request.query)

    logger.info(f"Generated response")

    return {"response": response}