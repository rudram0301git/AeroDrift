class Edge:
    """
    Represents a relationship between resources.
    """

    def __init__(
        self,
        source,
        target,
        relationship
    ):
        self.source = source
        self.target = target
        self.relationship = relationship

    def to_dict(self):

        return {
            "source": self.source,
            "target": self.target,
            "relationship": self.relationship
        }