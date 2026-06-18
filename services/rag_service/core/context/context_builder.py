from shared.config.settings import settings


class ContextBuilder:
    """
    Builds the final context passed to the LLM.
    """

    def build(self, results) -> str:
        # Apply final context limit
        results = results[:settings.FINAL_TOP_K]

        return "\n\n".join(
            r.payload.get("content", "")
            for r in results
        )