from pathlib import Path

from shared.logging.logger import get_logger

logger = get_logger("rag-service")


class DocumentLoader:

    SUPPORTED_DOCUMENT_TYPES = {
        ".txt",
        ".md",
    }

    def load(self, file_path: str) -> str:

        path = Path(file_path)

        self._validate(path)

        logger.info(
            "Loading document: %s",
            path.name,
        )

        content = path.read_text(
            encoding="utf-8"
        )

        logger.info(
            "Loaded '%s' (%d characters)",
            path.name,
            len(content),
        )

        return content

    def _validate(self, path: Path):

        if not path.exists():
            logger.error(
                "Document not found: %s",
                path,
            )
            raise FileNotFoundError(path)

        if path.suffix.lower() not in self.SUPPORTED_DOCUMENT_TYPES:
            logger.error(
                "Unsupported document type: %s",
                path.suffix,
            )
            raise ValueError(
                f"Unsupported document type: {path.suffix}"
            )