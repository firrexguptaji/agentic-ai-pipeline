import uuid
from pathlib import Path

from shared.logging.logger import get_logger

from services.rag_service.core.embedding.embedding import EmbeddingService
from services.rag_service.core.vector_db.qdrant import VectorDB

from .loader import DocumentLoader
from .chunker import TextChunker
from .models import IngestionResult

logger = get_logger("rag-service")


class IngestionPipeline:
    """
    Coordinates the document ingestion workflow.

    Document
        ↓
    Loader
        ↓
    Chunker
        ↓
    Embedding Service
        ↓
    Vector Database
    """

    def __init__(
        self,
        embedding_service,
        vector_db,
    ):
        self.loader = DocumentLoader()
        self.chunker = TextChunker()

        self.embedding_service = embedding_service
        self.vector_db = vector_db

    def ingest(self, file_path: str) -> IngestionResult:
        """
        Ingest a document into the vector database.

        Args:
            file_path: Path to the document.

        Returns:
            IngestionResult
        """

        logger.info("Starting ingestion: %s", file_path)

        path = Path(file_path)

        document_id = str(uuid.uuid4())

        text = self.loader.load(file_path)

        chunks = self.chunker.split(text)

        logger.info(
            "Processing %d chunk(s) for '%s'",
            len(chunks),
            path.name,
        )

        for chunk in chunks:

            chunk.metadata = self._build_metadata(
                document_id=document_id,
                filename=path.name,
                file_type=path.suffix,
                chunk_index=chunk.index,
                chunk_count=len(chunks),
                content=chunk.content,
            )

            chunk.embedding = self.embedding_service.embed(
                chunk.content
            )

            self.vector_db.insert(
                id=self._generate_point_id(),
                vector=chunk.embedding,
                payload=chunk.metadata,
            )

        logger.info(
            "Document '%s' ingested successfully.",
            path.name,
        )

        return IngestionResult(
            document_id=document_id,
            filename=path.name,
            chunks_processed=len(chunks),
        )

    @staticmethod
    def _generate_point_id() -> int:
        """
        Generate a unique integer ID for Qdrant.
        """
        return uuid.uuid4().int & ((1 << 63) - 1)

    @staticmethod
    def _build_metadata(
        document_id: str,
        filename: str,
        file_type: str,
        chunk_index: int,
        chunk_count: int,
        content: str,
    ) -> dict:
        """
        Build payload stored alongside vectors.
        """

        return {
            "document_id": document_id,
            "filename": filename,
            "file_type": file_type,
            "chunk_index": chunk_index,
            "chunk_count": chunk_count,
            "content": content,
        }