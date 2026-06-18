from typing import Any

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from shared.config.settings import settings
from shared.logging.logger import get_logger

logger = get_logger("rag-service")


class VectorDB:

    def __init__(self):

        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
        )

        self.collection_name = settings.QDRANT_COLLECTION

        self._create_collection()

    def _create_collection(self):

        try:

            self.client.get_collection(
                self.collection_name
            )

            logger.info(
                "Collection '%s' already exists.",
                self.collection_name,
            )

        except Exception:

            logger.info(
                "Creating collection '%s'.",
                self.collection_name,
            )

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=settings.VECTOR_SIZE,
                    distance=Distance.COSINE,
                ),
            )

    def insert(
        self,
        id: int,
        vector: list[float],
        payload: dict[str, Any],
    ):

        logger.debug(
            "Inserting vector %d",
            id,
        )

        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(
                    id=id,
                    vector=vector,
                    payload=payload,
                )
            ],
        )

    def search(
        self,
        query_vector: list[float],
        limit: int = settings.RETRIEVAL_TOP_K,
    ):

        logger.debug(
            "Searching top %d vectors.",
            limit,
        )

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit,
        )

        logger.info(
            "Retrieved %d result(s).",
            len(results.points),
        )

        return results.points