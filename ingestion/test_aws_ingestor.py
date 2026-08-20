from ingestion.aws_ingestor import AWSIngestor


def test_aws_ingestor_creation():
    ingestor = AWSIngestor()

    print("AWS Ingestor created successfully")
    print(f"Region: {ingestor.region}")


def test_ec2_ingestion():
    ingestor = AWSIngestor()

    instances = ingestor.get_ec2_instances()

    print(f"EC2 resources found: {len(instances)}")

    for instance in instances:
        print(instance)

def test_vpc_ingestion():
    ingestor = AWSIngestor()

    vpcs = ingestor.get_vpcs()

    print(f"VPC resources found: {len(vpcs)}")

    for vpc in vpcs:
        print(vpc)

if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()
    test_vpc_ingestion()

def test_subnet_ingestion():
    ingestor = AWSIngestor()

    subnets = ingestor.get_subnets()

    print(f"Subnet resources found: {len(subnets)}")

    for subnet in subnets:
        print(subnet)

if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()
    test_vpc_ingestion()
    test_subnet_ingestion()