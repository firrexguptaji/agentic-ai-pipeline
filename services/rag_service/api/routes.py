from fastapi import APIRouter

from services.rag_service.core.embedding.embedding import EmbeddingService
from services.rag_service.core.vector_db.qdrant import VectorDB
from services.rag_service.core.retrieval.retriever import Retriever
from services.rag_service.core.context.context_builder import ContextBuilder

from shared.config.settings import settings

router = APIRouter()

# ✅ Initialize components
embedder = EmbeddingService()
vector_db = VectorDB()
retriever = Retriever(embedder, vector_db)   # 🔥 FIXED
context_builder = ContextBuilder()


@router.post("/store")
def store(data: dict):
    text = data["text"]
    id = data["id"]

    vector = embedder.embed(text)

    vector_db.insert(
        id=id,
        vector=vector,
        payload={"text": text}
    )

    return {"status": "stored"}


@router.post("/retrieve")
def retrieve(data: dict):
    query = data["query"]

    # 🔥 Retriever already uses config internally
    results = retriever.retrieve(query)

    context = context_builder.build(results)

    return {
        "context": context,
        "results": [
            {
                "text": r.payload.get("text"),
                "score": r.score
            }
            for r in results
        ]
    }