from shared.config.settings import settings


class Retriever:
    def __init__(self, embedder, vector_db):
        self.embedder = embedder
        self.vector_db = vector_db

    def retrieve(self, query: str):
        query_vector = self.embedder.embed(query)

        results = self.vector_db.search(
            query_vector=query_vector,
            limit=settings.RETRIEVAL_TOP_K
        )

        # 🔥 filter
        filtered = [
            r for r in results
            if r.score > settings.SCORE_THRESHOLD
        ]

        # 🔥 sort
        filtered = sorted(filtered, key=lambda x: x.score, reverse=True)

        # 🔥 final selection
        return filtered[:settings.FINAL_TOP_K]