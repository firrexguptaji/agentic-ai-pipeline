from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

from services.agent_service.core.llm import LLMProvider
from services.agent_service.core.embedding.embedding import EmbeddingService




logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Agent Service")

llm = LLMProvider()
embedding_service = EmbeddingService()


class AgentRequest(BaseModel):
    query: str

@app.post("/generate")
def generate(request: AgentRequest):
    try:
        logger.info(f"Query: {request.query}")

        response = llm.generate(request.query)

        return {"response": response}

    except Exception as e:
        logger.error(f"Agent error: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Agent failed to process request"
        )
        
@app.post("/embed")
def embed_text(request: AgentRequest):
    try:
        vector = embedding_service.embed(request.query)
        return {"embedding": vector}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))