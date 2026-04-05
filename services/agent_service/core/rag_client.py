import requests
from shared.config.settings import settings


class RAGClient:
    def __init__(self):
        self.base_url = settings.RAG_SERVICE_URL

    def retrieve(self, query: str):
        response = requests.post(
            f"{self.base_url}/retrieve",
            json={
                "query": query,
                "top_k": settings.RETRIEVAL_TOP_K  # broad search
            },
            timeout=10
        )

        response.raise_for_status()
        return response.json()