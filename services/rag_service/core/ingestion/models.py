from dataclasses import dataclass, field
from typing import Any


@dataclass
class DocumentChunk:
    index: int
    content: str
    embedding: list[float] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class IngestionResult:
    document_id: str
    filename: str
    chunks_processed: int