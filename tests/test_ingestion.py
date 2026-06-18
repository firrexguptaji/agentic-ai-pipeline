from services.rag_service.core.ingestion.pipeline import (
    IngestionPipeline,
)
from services.rag_service.core.embedding.embedding import (
    EmbeddingService,
)
from services.rag_service.core.vector_db.qdrant import (
    VectorDB,
)


def test_document_ingestion():

    embedder = EmbeddingService()

    vector_db = VectorDB()

    pipeline = IngestionPipeline(
        embedding_service=embedder,
        vector_db=vector_db,
    )

    result = pipeline.ingest(
        "tests/sample.txt"
    )

    assert result.filename == "sample.txt"

    assert result.document_id is not None

    assert result.chunks_processed > 0

    print(result)