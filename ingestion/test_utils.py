def test_normalization():

    resource = normalize_resource(
        resource_id="example",
        resource_type="aws_instance",
        provider="Terraform",
        region="",
        state="configured"
    )

    print("Normalized resource:")
    print(resource)

    print("Resource normalization completed successfully")

from ingestion.utils import validate_resource, validate_resources


def test_resource_validation():

    resources = []

    valid_resources = validate_resources(resources)

    print("Resource validation completed successfully")
    print("Valid resources:", len(valid_resources))


if __name__ == "__main__":
    test_resource_validation()

def test_validation_function():

    print("Testing resource validation...")

    result = validate_resource(None)

    if result is False:
        print("Validation test passed")
    else:
        print("Validation test failed")


if __name__ == "__main__":
    test_resource_validation()
    test_validation_function()