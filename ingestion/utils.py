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

def normalize_resource(
    resource_id,
    resource_type,
    provider,
    region="",
    state=""
):
    """Create a common CloudResource format."""

    return CloudResource(
        resource_id=resource_id,
        resource_type=resource_type,
        provider=provider,
        region=region,
        state=state
    )