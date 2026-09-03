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