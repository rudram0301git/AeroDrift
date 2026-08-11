"""
AeroDrift - Ingestion Module

This package handles the collection and ingestion of cloud
infrastructure data from AWS, GCP, and Terraform.
"""

from .aws_ingestor import AWSIngestor
from .gcp_ingestor import GCPIngestor
from .terraform_ingestor import TerraformIngestor

__all__ = [
    "AWSIngestor",
    "GCPIngestor",
    "TerraformIngestor",
]

__version__ = "1.0.0"