import boto3

from ingestion.models import CloudResource


class AWSIngestor:

    def __init__(self, region="ap-south-1"):
        self.region = region

        self.ec2 = boto3.client(
            "ec2",
            region_name=self.region
        )

    def test_connection(self):
        """Test AWS connection."""

        response = self.ec2.describe_regions()

        return {
            "status": "success",
            "regions_available": len(response["Regions"])
        }

    def get_ec2_instances(self):
        """Collect basic EC2 instance information."""

        response = self.ec2.describe_instances()

        instances = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:

                resource = CloudResource(
                    resource_id=instance.get("InstanceId", ""),
                    resource_type="EC2",
                    provider="AWS",
                    region=self.region,
                    state=instance.get("State", {}).get("Name", ""),
                    instance_type=instance.get("InstanceType", ""),
                    vpc_id=instance.get("VpcId", ""),
                    subnet_id=instance.get("SubnetId", "")
                )

                instances.append(resource)

        return instances

    def get_vpcs(self):
        """Collect basic VPC information."""

        response = self.ec2.describe_vpcs()

        vpcs = []

        for vpc in response["Vpcs"]:
            resource = CloudResource(
                resource_id=vpc.get("VpcId", ""),
                resource_type="VPC",
                provider="AWS",
                region=self.region,
                state=vpc.get("State", ""),
                cidr_block=vpc.get("CidrBlock", "")
            )

            vpcs.append(resource)

        return vpcs

    def get_subnets(self):
         """Collect basic subnet information."""

         response = self.ec2.describe_subnets()

         subnets = []

         for subnet in response["Subnets"]:
            resource = CloudResource(
                resource_id=subnet.get("SubnetId", ""),
                resource_type="SUBNET", 
                provider="AWS",
                region=self.region,
                state="available",
                vpc_id=subnet.get("VpcId", ""),
                subnet_id=subnet.get("SubnetId", ""),
                cidr_block=subnet.get("CidrBlock", "")
            )

            subnets.append(resource)

         return subnets    

    def get_security_groups(self):
        """Collect basic Security Group information."""

        response = self.ec2.describe_security_groups()

        security_groups = []

        for group in response["SecurityGroups"]:
            resource = CloudResource(
                resource_id=group.get("GroupId", ""),
                resource_type="SECURITY_GROUP",
                provider="AWS",
                region=self.region,
                vpc_id=group.get("VpcId", ""),
                description=group.get("Description", "")
            )

            security_groups.append(resource)

        return security_groups