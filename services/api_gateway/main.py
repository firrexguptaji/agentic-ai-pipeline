from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import requests
import time

from shared.config.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="API Gateway")


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query_handler(request: QueryRequest):
    try:
        if not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        logger.info(f"Received query: {request.query}")

        start = time.time()

        response = requests.post(
            settings.AGENT_SERVICE_URL,
            json={"query": request.query},
            timeout=settings.REQUEST_TIMEOUT
        )

        latency = round(time.time() - start, 2)
        logger.info(f"Agent response time: {latency}s")

        if response.status_code != 200:
            raise Exception(f"Agent service error: {response.text}")

        data = response.json()

        if "response" not in data:
            raise Exception("Invalid response from agent service")

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
            detail=f"Gateway error: {str(e)}"
        )