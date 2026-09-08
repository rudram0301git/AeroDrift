class RemediationPlanner:
    """
    Create a simple remediation plan.
    """

    def create_plan(self, differences):

        plan = []

        for difference in differences:

            action = {
                "action": "UPDATE_RESOURCE",
                "difference": difference
            }

            plan.append(action)

        return plan