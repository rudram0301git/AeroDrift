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

def validate_resource(resource):
    """Validate basic cloud resource information."""

    if resource is None:
        return False

    if not resource.resource_id:
        return False

    if not resource.resource_type:
        return False

    if not resource.provider:
        return False

    return True


def validate_resources(resources):
    """Return only valid resources."""

    valid_resources = []

    for resource in resources:
        if validate_resource(resource):
            valid_resources.append(resource)

    return valid_resources