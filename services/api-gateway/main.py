from fastapi import FastAPI
from pydantic import BaseModel
import logging

# -----------------------
# Logging Setup
# -----------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------
# App Init
# -----------------------
app = FastAPI(title="API Gateway")

# -----------------------
# Request Schema
# -----------------------
class QueryRequest(BaseModel):
    query: str

# -----------------------
# Routes
# -----------------------
@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/query")
def query_handler(request: QueryRequest):
    logger.info(f"Received query: {request.query}")

    # Dummy response (for now)
    response = {
        "response": f"Dummy response for: {request.query}"
    }

    logger.info(f"Sending response: {response}")

    return response