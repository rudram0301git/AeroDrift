class TerraformIngestor:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """Read the Terraform file."""

        with open(self.file_path, "r") as file:
            content = file.read()

        return content