from ingestion import run_ingestion


def test_unified_ingestion():

    resources = run_ingestion()

    print("Unified ingestion completed successfully")
    print("Total resources found:", len(resources))


if __name__ == "__main__":
    test_unified_ingestion()