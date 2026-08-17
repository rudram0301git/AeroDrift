from ingestion.aws_ingestor import AWSIngestor


def test_aws_ingestor_creation():
    ingestor = AWSIngestor()

    print("AWS Ingestor created successfully")
    print(f"Region: {ingestor.region}")


if __name__ == "__main__":
    test_aws_ingestor_creation()