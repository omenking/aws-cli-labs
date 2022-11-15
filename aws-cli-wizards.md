```
aws dynamodb wizard new-table
```

## Creating our on Wizard

Its not documented but you can create your own wizards.
All we need to do is symlink folders into the wizards directory:

```
/usr/local/aws-cli/v2/current/dist/awscli/customizations/wizard/wizards
```

```
mkdir s3
```

We just need to follow the structure of these files:

https://github.com/aws/aws-cli/tree/v2/awscli/customizations/wizard/wizards


https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html

```
version: "0.2"
title: Create an S3 Bucket
description: This is a wizard to create an S3 bucket
plan:
  intro:
    shortname: Intro
    Description: Create a new S3 Bucket
    values:
      bucket_name: 
        type: prompt
        description: Bucket Name
      region:
        type: prompt
        choices:
          - actual_value: us-east-1
            display: North Virgina
          - actual_value: ca-central-1
            display: Canada Central
  preview:
    shortname: Preview
    description: Preview results
    values:
      preview_cli_command_value:
        type: template
        value: |
          aws s3 mb 's3://{bucket_name}' --region '{region}'
      preview_value:
        type: template
        value: |
          {%if {preview_type} == preview_cli_command %}
          {preview_cli_command_value}
          {% endif %}
      preview_type:
        type: prompt
        description: Select an preview format
        choices:
          - display: None
            actual_value: preview_none
          - display: AWS CLI command
            actual_value: preview_cli_command
        details:
          value: preview_value
          visible: True
          description: "Preview"
  __DONE__:
execute:
  default:
    - type: apicall
      operation: CreateBucket
      params:
        Bucket: "{bucket_name}"
__OUTPUT__:
  value: |
    Wizard successfully created an S3 Bucket: s3://{bucket_name}
    {% if {preview_type} == preview_cli_command %}
    Steps to create function is equivalent to running the following sample AWS CLI commands:
    {preview_cli_command_value}
    {% endif %}
```