from fastapi import FastAPI
import logging

from services.rag_service.api.routes import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="RAG Service")

# Include routes
app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "RAG service is running"}