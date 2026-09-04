class Node:
    """
    Represents a resource in the topology.
    """

    def __init__(
        self,
        resource_id,
        resource_type
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type

    def to_dict(self):

        return {
            "resource_id": self.resource_id,
            "resource_type": self.resource_type
        }