import boto3


class AWSIngestor:
    def __init__(self, region="ap-south-1"):
        self.region = region
        self.ec2 = boto3.client(
            "ec2",
            region_name=self.region
        )

    def get_instances(self):
        response = self.ec2.describe_instances()

        instances = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append({
                    "id": instance["InstanceId"],
                    "state": instance["State"]["Name"],
                    "type": instance["InstanceType"]
                })

        return instances

    def get_security_groups(self):
        response = self.ec2.describe_security_groups()

        security_groups = []

        for group in response["SecurityGroups"]:
            security_groups.append({
                "id": group["GroupId"],
                "name": group["GroupName"],
                "description": group.get("Description", "")
            })

        return security_groups