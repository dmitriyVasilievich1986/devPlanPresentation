locals {
  lambda_name = "lambda_test"
}

data "archive_file" "lambda_zip" {
  excludes = [
    ".env.",
    ".terraform",
    ".terraform.lock.hcl",
    "${local.lambda_name}.zip",
  ]
  
  output_path = "${path.module}/${local.lambda_name}.zip"
  source_dir  = "${path.module}/lambdas"
  type        = "zip"
}

resource "aws_lambda_function" "lambda_test" {
  function_name    = local.lambda_name
  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  role             = "arn:aws:iam::409693173775:role/service-role/APILambda-role-74y8skgd"
  handler          = "main.handler"
  runtime          = "python3.12"
  timeout          = 4
}
