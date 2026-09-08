from .graph import CloudGraph
from .nodes import Node
from .edges import Edge


class GraphBuilder:
    """
    Build topology graph from cloud resources.
    """

    def build(self, resources):

        graph = CloudGraph()

        # Create nodes
        for resource in resources:

            node = Node(
                resource.resource_id,
                resource.resource_type
            )

            graph.add_node(node)

        # Create relationships
        for resource in resources:

            vpc_id = getattr(resource, "vpc_id", None)

            if vpc_id:

                edge = Edge(
                    source=resource.resource_id,
                    target=vpc_id,
                    relationship="BELONGS_TO"
                )

                graph.add_edge(edge)

        return graph