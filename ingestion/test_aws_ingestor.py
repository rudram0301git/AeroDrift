from ingestion.aws_ingestor import AWSIngestor


def test_aws_ingestor():
    ingestor = AWSIngestor()
    print("AWS Ingestor created successfully")


if __name__ == "__main__":
    test_aws_ingestor()