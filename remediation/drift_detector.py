class DriftDetector:
    """
    Detect simple infrastructure differences.
    """

    def compare(self, current, desired):

        differences = []

        if current != desired:

            differences.append({
                "current": current,
                "desired": desired
            })

        return differences