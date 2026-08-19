from dataclasses import dataclass


@dataclass
class CloudResource:
    resource_id: str
    resource_type: str
    provider: str
    region: str
    state: str = ""
    instance_type: str = ""
    vpc_id: str = ""
    subnet_id: str = ""
    cidr_block: str = ""