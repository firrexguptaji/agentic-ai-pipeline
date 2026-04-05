from shared.config.settings import settings


class ContextBuilder:
    def build(self, results):
        # optional safety limit
        results = results[:settings.FINAL_TOP_K]

        return "\n\n".join(
            [r.payload.get("text", "") for r in results]
        )