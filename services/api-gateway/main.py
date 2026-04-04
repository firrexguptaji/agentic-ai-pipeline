from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="API Gateway")

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_handler(request: QueryRequest):
    try:
        logger.info(f"Received query: {request.query}")

        return {
            "response": f"Dummy response for: {request.query}"
        }

    except Exception as e:
        logger.error(f"API error: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )