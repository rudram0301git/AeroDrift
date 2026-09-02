import logging


def setup_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def log_resource(resource) -> None:
    logging.info(
        "Resource: %s | Type: %s | Provider: %s",
        resource.resource_id,
        resource.resource_type,
        resource.provider,
    )