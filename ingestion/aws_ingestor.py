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

    def get_ec2_instances(self):
        """Collect EC2 instance information."""

        response = self.ec2.describe_instances()

        instances = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append({
                    "instance_id": instance.get("InstanceId"),
                    "instance_type": instance.get("InstanceType"),
                    "state": instance.get("State", {}).get("Name"),
                    "availability_zone": instance.get("Placement", {}).get("AvailabilityZone"),
                    "vpc_id": instance.get("VpcId"),
                    "subnet_id": instance.get("SubnetId")
                })

        return instances