from fastapi import FastAPI


from services.rag_service.api.routes import router
from shared.middleware.request_id import request_id_middleware
from shared.logging.logger import get_logger

logger = get_logger("rag-service")

app = FastAPI(title="RAG Service")
app.middleware("http")(request_id_middleware)

# Include routes
app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "RAG service is running"}