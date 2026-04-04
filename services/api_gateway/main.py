from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from shared.config.settings import settings
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="API Gateway")

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_handler(request: QueryRequest):
    try:
        logger.info(f"Received query: {request.query}")

        # 🔥 Call Agent Service
        logger.info("Waiting for agent response...")
        response = requests.post(
            settings.AGENT_SERVICE_URL,
            json={"query": request.query},
            timeout=settings.REQUEST_TIMEOUT
        )

        if response.status_code != 200:
            raise Exception(f"Agent service error: {response.text}")

        data = response.json()

        logger.info("Response received from agent")

        return data

    except requests.exceptions.Timeout:
        logger.error("Agent service timeout")

        raise HTTPException(
            status_code=504,
            detail="Agent service timeout"
        )

    except Exception as e:
        logger.error(f"API error: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Failed to process request"
        )