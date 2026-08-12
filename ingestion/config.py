import os


AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")