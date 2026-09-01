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

    def get_route_tables(self):
         """Collect basic Route Table information."""

         response = self.ec2.describe_route_tables()

         route_tables = []

         for table in response["RouteTables"]:
            resource = CloudResource(
                resource_id=table.get("RouteTableId", ""),
                resource_type="ROUTE_TABLE",
                provider="AWS",
                region=self.region,
                vpc_id=table.get("VpcId", ""),
                route_table_id=table.get("RouteTableId", "")
            )

            route_tables.append(resource)

         return route_tables

    def get_network_interfaces(self):
        """Collect basic Network Interface information."""

        response = self.ec2.describe_network_interfaces()

        interfaces = []

        for interface in response["NetworkInterfaces"]:
            resource = CloudResource(
                resource_id=interface.get("NetworkInterfaceId", ""),
                resource_type="NETWORK_INTERFACE",
                provider="AWS",
                region=self.region,
                state=interface.get("Status", ""),
                vpc_id=interface.get("VpcId", ""),
                subnet_id=interface.get("SubnetId", ""),
                private_ip=interface.get("PrivateIpAddress", ""),
                description=interface.get("Description", "")
            )

            interfaces.append(resource)

        return interfaces

    def get_rds_instances(self):
        """Collect basic RDS information."""

        rds = boto3.client(
            "rds",
            region_name=self.region
        )

        response = rds.describe_db_instances()

        databases = []

        for db in response["DBInstances"]:
            resource = CloudResource(
                resource_id=db.get("DBInstanceIdentifier", ""),
                resource_type="RDS",
                provider="AWS",
                region=self.region,
                state=db.get("DBInstanceStatus", ""),
                vpc_id=db.get("DBSubnetGroup", {}).get("VpcId", ""),
                database_engine=db.get("Engine", "")
            )

            databases.append(resource)

        return databases

    def get_s3_buckets(self):
         """Collect basic S3 bucket information."""

         s3 = boto3.client("s3")

         try:
           response = s3.list_buckets()
         except Exception as e:
           print("Error fetching S3 buckets:", e)
         return []

         buckets = []

         for bucket in response.get("Buckets", []):
            resource = CloudResource(
                resource_id=bucket.get("Name", ""),
                resource_type="S3_BUCKET",
                provider="AWS",
                region=self.region,
                state="available"
            )

            buckets.append(resource)

         return buckets

    def get_all_resources(self):
         """Collect all supported AWS resources."""

         resources = []

         resources.extend(self.get_ec2_instances())
         resources.extend(self.get_vpcs())
         resources.extend(self.get_subnets())
         resources.extend(self.get_security_groups())
         resources.extend(self.get_route_tables())
         resources.extend(self.get_network_interfaces())
         resources.extend(self.get_rds_instances())
         resources.extend(self.get_s3_buckets())

         print("AWS resource ingestion completed.")
         return resources

    def get_resource_summary(self):
        """Return a simple summary of AWS resources."""

        resources = self.get_all_resources()

        summary = {}

        for resource in resources:
         resource_type = resource.resource_type
        summary[resource_type] = summary.get(resource_type, 0) + 1

        print("AWS Resource Summary:")

        for resource_type, count in summary.items():
         print(f"{resource_type}: {count}")

         return summary