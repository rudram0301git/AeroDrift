from ingestion.aws_ingestor import AWSIngestor
from topology.builder import GraphBuilder


def test_topology():

    print("Starting topology test...")

    # Get cloud resources
    ingestor = AWSIngestor()
    resources = ingestor.get_all_resources()

    print("Resources found:", len(resources))

    # Build topology graph
    builder = GraphBuilder()
    graph = builder.build(resources)

    print("\nTopology graph created successfully.")

    # Display graph
    graph.show_graph()

    print("\nTopology test completed successfully.")


if __name__ == "__main__":
    test_topology()