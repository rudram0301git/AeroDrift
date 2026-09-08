import re


class TerraformIngestor:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """Read the Terraform file."""

        with open(self.file_path, "r") as file:
            content = file.read()

        return content

    def extract_resources(self):
        """Extract Terraform resources."""

        content = self.read_file()

        resources = re.findall(
            r'resource\s+"([^"]+)"\s+"([^"]+)"',
            content
        )

        return resources