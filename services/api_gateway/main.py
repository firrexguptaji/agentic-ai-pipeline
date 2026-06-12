from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import time

from shared.config.settings import settings
from shared.logging.logger import get_logger
from shared.middleware.request_id import request_id_middleware


logger = get_logger("api-gateway")

app = FastAPI(title="API Gateway")
app.middleware("http")(request_id_middleware)


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
        logger.exception("Agent service timeout")

        raise HTTPException(
            status_code=504,
            detail="Agent service timeout"
        )

    except Exception as e:
        logger.exception("API error")

        raise HTTPException(
            status_code=500,
            detail=f"Gateway error: {str(e)}"
        )