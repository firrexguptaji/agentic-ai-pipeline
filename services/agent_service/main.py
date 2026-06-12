from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


from services.agent_service.core.llm import LLMProvider
from services.agent_service.core.rag_client import RAGClient
from shared.config.settings import settings
from shared.logging.logger import get_logger
from shared.middleware.request_id import request_id_middleware


logger = get_logger("agent-service")

app = FastAPI(title="Agent Service")
app.middleware("http")(request_id_middleware)

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
        logger.info(f"RAG Response: {rag_response}")

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
        logger.exception("Agent processing failed")

        raise HTTPException(
            status_code=500,
            detail="Agent failed to process request"
        )