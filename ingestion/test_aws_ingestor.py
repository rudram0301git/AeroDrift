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

def test_security_group_ingestion():
    ingestor = AWSIngestor()

    security_groups = ingestor.get_security_groups()

    print(f"Security Groups found: {len(security_groups)}")

    for group in security_groups:
        print(group)

if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()
    test_vpc_ingestion()
    test_subnet_ingestion()
    test_security_group_ingestion()

def test_route_table_ingestion():
    ingestor = AWSIngestor()

    route_tables = ingestor.get_route_tables()

    print(f"Route Tables found: {len(route_tables)}")

    for route_table in route_tables:
        print(route_table)

if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()
    test_vpc_ingestion()
    test_subnet_ingestion()
    test_security_group_ingestion()
    test_route_table_ingestion()

def test_network_interface_ingestion():
    ingestor = AWSIngestor()

    interfaces = ingestor.get_network_interfaces()

    print(f"Network Interfaces found: {len(interfaces)}")

    for interface in interfaces:
        print(interface)

if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()
    test_vpc_ingestion()
    test_subnet_ingestion()
    test_security_group_ingestion()
    test_route_table_ingestion()
    test_network_interface_ingestion()

def test_rds_ingestion():
    ingestor = AWSIngestor()

    databases = ingestor.get_rds_instances()

    print(f"RDS resources found: {len(databases)}")

    for database in databases:
        print(database)

if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()
    test_vpc_ingestion()
    test_subnet_ingestion()
    test_security_group_ingestion()
    test_route_table_ingestion()
    test_network_interface_ingestion()
    test_rds_ingestion()

def test_s3_ingestion():
    ingestor = AWSIngestor()

    buckets = ingestor.get_s3_buckets()

    print("S3 buckets found: {len(buckets)}")

    for bucket in buckets:
        print(bucket)

    print("S3 ingestion test completed successfully")

if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()
    test_vpc_ingestion()
    test_subnet_ingestion()
    test_security_group_ingestion()
    test_route_table_ingestion()
    test_network_interface_ingestion()
    test_rds_ingestion()
    test_s3_ingestion()

def test_all_resources():
    ingestor = AWSIngestor()

    resources = ingestor.get_all_resources()

    print("Total AWS resources found:", len(resources))

    for resource in resources:
        print(resource)

if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()
    test_vpc_ingestion()
    test_subnet_ingestion()
    test_security_group_ingestion()
    test_route_table_ingestion()
    test_network_interface_ingestion()
    test_rds_ingestion()
    test_s3_ingestion()
    test_all_resources()

def test_resource_summary():
    ingestor = AWSIngestor()

    summary = ingestor.get_resource_summary()

    print("AWS Resource Summary:")

    for resource_type, count in summary.items():
        print(resource_type, ":", count)

if __name__ == "__main__":
    test_aws_ingestor_creation()
    test_ec2_ingestion()
    test_vpc_ingestion()
    test_subnet_ingestion()
    test_security_group_ingestion()
    test_route_table_ingestion()
    test_network_interface_ingestion()
    test_rds_ingestion()
    test_s3_ingestion()
    test_all_resources()
    test_resource_summary()