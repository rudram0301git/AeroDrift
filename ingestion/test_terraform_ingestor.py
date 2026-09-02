from ingestion.terraform_ingestor import TerraformIngestor


def test_terraform_file():

    ingestor = TerraformIngestor("ingestion/main.tf")

    content = ingestor.read_file()

    print("Terraform file content:")
    print(content)

    print("Terraform file parsing completed successfully")


if __name__ == "__main__":
    test_terraform_file()

def test_terraform_resources():

    ingestor = TerraformIngestor("main.tf")

    resources = ingestor.extract_resources()

    print("Terraform resources found:")

    for resource_type, resource_name in resources:
        print(
            f"Type: {resource_type}, "
            f"Name: {resource_name}"
        )

    print("Terraform resource extraction completed successfully")

if __name__ == "__main__":
    test_terraform_file()
    test_terraform_resources()