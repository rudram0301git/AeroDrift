class RemediationExecutor:
    """
    Execute remediation actions.
    """

    def execute(self, plan):

        for action in plan:

            print(
                "Executing:",
                action["action"]
            )

            print(
                "Details:",
                action["difference"]
            )

        print("Remediation completed.")