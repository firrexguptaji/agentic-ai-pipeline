from services.rag_service.core.context.context_builder import ContextBuilder
from services.rag_service.core.embedding.embedding import EmbeddingService
from services.rag_service.core.retrieval.retriever import Retriever
from services.rag_service.core.vector_db.qdrant import VectorDB


def test_document_retrieval():
    embedder = EmbeddingService()
    vector_db = VectorDB()

    retriever = Retriever(embedder, vector_db)
    context_builder = ContextBuilder()

    results = retriever.retrieve("What is Python?")

    assert len(results) > 0

    context = context_builder.build(results)

    assert "Python" in context