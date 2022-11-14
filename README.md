# AWS CLI Labs

## Configuration

In order to use the AWS CLI we need to configure credentials.
We can set our eviroment variables.

```sh
export AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=ca-central-1
```

If want these enviroment variables to persist in future workspace
launches then set them in gitpod's enviroment variables manager.

```sh
gp env AWS_ACCESS_KEY_ID
gp env AWS_SECRET_ACCESS_KEY=
gp env AWS_DEFAULT_REGION=ca-central-1
```


## Hands-on Labs

These AWS CLI Hands on Labs for Build on Live AWS re:Invent 2022

- [AWS CLI Autoprompt](aws-cli-autoprompt.md)
- [AWS CLI Filter and Query](aws-cli-filter-and-query.md)
- [JP and JQ with AWS CLI](jp-and-jq-with-aws-cli.md)
- [Chaining AWS CLI with X-Args](chaining-xargs.md)
- [AWS CLI Aliases](aws-cli-aliases.md)
- [AWS CLI Wizards](aws-cli-wizards.md)
- [AWS CLI Skeleton Templates](aws-cli-skeleton-templates.md)
- [AWS-CLI-with-LocalStack](aws-cli-localstack.md)