import boto3


class AWSIngestor:
    """Handles connection to AWS services."""

    def __init__(self, region="ap-south-1"):
        self.region = region

        self.ec2 = boto3.client(
            "ec2",
            region_name=self.region
        )

    def test_connection(self):
        """Test whether AWS EC2 API is accessible."""
        response = self.ec2.describe_regions()

        return {
            "status": "success",
            "regions_available": len(response["Regions"])
        }