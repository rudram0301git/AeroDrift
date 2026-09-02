terraform {
  required_version = ">= 1.0"
}

resource "aws_s3_bucket" "example" {
  bucket = "aerodrift-example-bucket"
}