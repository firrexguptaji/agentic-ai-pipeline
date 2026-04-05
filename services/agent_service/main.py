from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

from services.agent_service.core.llm import LLMProvider
from services.agent_service.core.rag_client import RAGClient
from shared.config.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Agent Service")

llm = LLMProvider()
rag_client = RAGClient()


class AgentRequest(BaseModel):
    query: str


@app.post("/generate")
def generate(request: AgentRequest):
    try:
        query = request.query
        logger.info(f"Query: {query}")

        # 🔹 Step 1: Get context from RAG service
        rag_response = rag_client.retrieve(query)

        context = rag_response.get("context", "")

        if not context:
            return {
                "query": query,
                "response": "No relevant information found."
            }

        # 🔹 Step 2: Build prompt
        prompt = f"""
        {settings.SYSTEM_PROMPT}
        
        Context:
        {context}
        
        Question:
        {query}
        """

        # 🔹 Step 3: Generate response
        response = llm.generate(prompt)

        return {
            "query": query,
            "response": response,
            "sources": rag_response.get("results", [])[:settings.MAX_SOURCES]
        }

    except Exception as e:
        logger.error(f"Agent error: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Agent failed to process request"
        )