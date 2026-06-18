import os
import tempfile

from fastapi import APIRouter, File, UploadFile

from services.rag_service.core.context.context_builder import ContextBuilder
from services.rag_service.core.embedding.embedding import EmbeddingService
from services.rag_service.core.ingestion.pipeline import IngestionPipeline
from services.rag_service.core.retrieval.retriever import Retriever
from services.rag_service.core.vector_db.qdrant import VectorDB

router = APIRouter()

# Initialize shared services
embedder = EmbeddingService()
vector_db = VectorDB()
retriever = Retriever(embedder, vector_db)
context_builder = ContextBuilder()

# Initialize ingestion pipeline using shared services
pipeline = IngestionPipeline(
    embedding_service=embedder,
    vector_db=vector_db,
)


@router.post("/store")
def store(data: dict):
    text = data["text"]
    point_id = data["id"]

    vector = embedder.embed(text)

    vector_db.insert(
        id=point_id,
        vector=vector,
        payload={
            "content": text
        },
    )

    return {"status": "stored"}


@router.post("/retrieve")
def retrieve(data: dict):
    query = data["query"]

    results = retriever.retrieve(query)

    context = context_builder.build(results)

    return {
        "context": context,
        "results": [
            {
                "content": r.payload.get("content"),
                "score": r.score,
            }
            for r in results
        ],
    }


@router.post("/ingest")
async def ingest_document(
    file: UploadFile = File(...),
):
    """
    Upload and ingest a TXT or Markdown document.
    """

    temp_path = None

    try:
        suffix = os.path.splitext(file.filename)[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix,
        ) as temp_file:
            temp_file.write(await file.read())
            temp_path = temp_file.name

        result = pipeline.ingest(temp_path)

        return {
            "status": "success",
            "document_id": result.document_id,
            "filename": result.filename,
            "chunks_processed": result.chunks_processed,
        }

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)