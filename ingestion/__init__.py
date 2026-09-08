from .aws_ingestor import AWSIngestor
from .terraform_ingestor import TerraformIngestor


def run_ingestion(terraform_file=None):
    """Run the available ingestion sources."""

    resources = []

    # AWS ingestion
    aws_ingestor = AWSIngestor()
    aws_resources = aws_ingestor.get_all_resources()
    resources.extend(aws_resources)

    # Terraform ingestion
    if terraform_file:
        terraform_ingestor = TerraformIngestor(terraform_file)

        try:
            terraform_resources = terraform_ingestor.extract_resources()
            resources.extend(terraform_resources)
        except AttributeError:
            print("Terraform resource extraction is not available.")

    return resources


__all__ = [
    "AWSIngestor",
    "TerraformIngestor",
    "run_ingestion"
]

__version__ = "0.1.0"