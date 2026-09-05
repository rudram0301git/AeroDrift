class CloudGraph:
    """
    Simple cloud topology graph.
    """

    def __init__(self):

        self.nodes = []
        self.edges = []

    def add_node(self, node):

        self.nodes.append(node)

    def add_edge(self, edge):

        self.edges.append(edge)

    def show_graph(self):

        print("\nNodes:")

        for node in self.nodes:
            print(
                node.resource_id,
                node.resource_type
            )

        print("\nEdges:")

        for edge in self.edges:
            print(
                edge.source,
                "->",
                edge.target,
                "(",
                edge.relationship,
                ")"
            )