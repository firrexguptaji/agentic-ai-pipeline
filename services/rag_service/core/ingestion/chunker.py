from shared.config.settings import settings
from shared.logging.logger import get_logger

from .models import DocumentChunk

logger = get_logger("rag-service")

logger = get_logger("rag-service")


class TextChunker:
    """
    Splits text into overlapping chunks suitable for embedding generation.
    """

    def __init__(
        self,
        chunk_size: int = settings.CHUNK_SIZE,
        overlap: int = settings.CHUNK_OVERLAP,
    ):
        self._validate_config(chunk_size, overlap)

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str) -> list[DocumentChunk]:
        """
        Split text into overlapping chunks.

        Args:
            text: Input document text.

        Returns:
            List of DocumentChunk objects.
        """

        if not text.strip():
            logger.warning(
                "Cannot chunk an empty document."
            )
            return []

        chunks: list[DocumentChunk] = []

        step_size = self.chunk_size - self.overlap

        for index, start in enumerate(
            range(0, len(text), step_size)
        ):
            content = text[start:start + self.chunk_size]

            if content.strip():
                chunks.append(
                    self._create_chunk(
                        index=index,
                        content=content,
                    )
                )

        logger.info(
            "Generated %d chunk(s) "
            "(chunk_size=%d, overlap=%d)",
            len(chunks),
            self.chunk_size,
            self.overlap,
        )

        return chunks

    @staticmethod
    def _validate_config(
        chunk_size: int,
        overlap: int,
    ) -> None:
        """
        Validate chunking configuration.
        """

        if chunk_size <= 0:
            raise ValueError(
                "Chunk size must be greater than zero."
            )

        if overlap < 0:
            raise ValueError(
                "Chunk overlap cannot be negative."
            )

        if overlap >= chunk_size:
            raise ValueError(
                "Chunk overlap must be smaller than chunk size."
            )

    @staticmethod
    def _create_chunk(
        index: int,
        content: str,
    ) -> DocumentChunk:
        """
        Create a document chunk.
        """

        return DocumentChunk(
            index=index,
            content=content,
        )