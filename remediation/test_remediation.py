from .drift_detector import DriftDetector
from .remediation_planner import RemediationPlanner
from .remediation_executor import RemediationExecutor


def test_remediation():

    print("Starting remediation test...")

    current = {
        "instance_type": "t2.micro"
    }

    desired = {
        "instance_type": "t3.micro"
    }

    detector = DriftDetector()
    differences = detector.compare(current, desired)

    print("Differences found:", differences)

    planner = RemediationPlanner()
    plan = planner.create_plan(differences)

    print("Remediation plan:", plan)

    executor = RemediationExecutor()
    executor.execute(plan)

    print("Remediation test completed successfully.")


if __name__ == "__main__":
    test_remediation()