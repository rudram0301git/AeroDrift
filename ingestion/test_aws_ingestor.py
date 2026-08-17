from ingestion.aws_ingestor import AWSIngestor


def test_aws_ingestor_creation():
    ingestor = AWSIngestor()

    print("AWS Ingestor created successfully")
    print(f"Region: {ingestor.region}")


def test_ec2_ingestion():
    ingestor = AWSIngestor()

    instances = ingestor.get_ec2_instances()

    print(f"EC2 instances found: {len(instances)}")

    for instance in instances:
        print(instance)


if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()