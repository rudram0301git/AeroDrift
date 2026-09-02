from ingestion.terraform_ingestor import TerraformIngestor


def test_terraform_file():

    ingestor = TerraformIngestor("ingestion/main.tf")

    content = ingestor.read_file()

    print("Terraform file content:")
    print(content)

    print("Terraform file parsing completed successfully")


if __name__ == "__main__":
    test_terraform_file()