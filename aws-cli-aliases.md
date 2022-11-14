# AWS CLI Aliases

## What is AWS CLI Aliases?

AWS CLI Aliases is similar to bash aliases.

- You can write your own toplevel shorthands for commmands or bash scripts.

## Create an Alias File

```sh
mkdir -p ~/.aws/cli
touch ~/.aws/cli/alias
gp open ~/.aws/cli/alias
```

We'll add the following:

```toml
[toplevel]
vpcw2 = ec2 describe-vpcs --query "Vpcs[*].[CidrBlock,VpcId]" --output table --region us-west-2
```

## Run our alias

We'll run our alias which will describe VPCs in US-West-2

```
aws vpcw2
```

## Hot-swapping Alias files

If you are updating or want to swap alises out for specific jobs
I created this bash script.

Create a place to store the bash script

```
mkdir -p bin
touch bin/aws-alias
chmod u+x bin/aws-alias
gp open bin/aws-alias
```

```sh
#!/usr/bin/env bash
set -e

if [ -z "$1" ]; then
  ALIAS_FILE_NAME=$1
else
  ALIAS_FILE_NAME=default
fi

alias_path="$(realpath ..)/aws/aliases/$ALIAS_FILE_NAME.toml"

cp alias_path ~/.aws/cli/alias
```

Lets create a new file:

```sh
mkdir -p aws/aliases
touch aws/aliases/default.toml
gp open aws/aliases/default.toml
```

Lets have the following

```toml
[toplevel]
vpcw2 = ec2 describe-vpcs --query "Vpcs[*].[CidrBlock,VpcId]" --output table --region us-west-2

amazon-linux-amis = ec2 describe-images \
    --filter \
      Name=owner-alias,Values=amazon \
      Name=name,Values="amzn-ami-hvm-*" \
      Name=architecture,Values=x86_64 \
      Name=virtualization-type,Values=hvm \
      Name=root-device-type,Values=ebs \
      Name=block-device-mapping.volume-type,Values=gp2 \
    --query "reverse(sort_by(Images, &CreationDate))[*].[ImageId,Name,Description]" \
    --output text
```

> Note that our aliases can be multline with the `\`

Lets load our update alias file  and test our new command

```sh
./bin/aws-alias
aws amazon-linux-amis
```

Lets create an alternate file

```sh
mkdir -p aws/aliases
touch aws/aliases/serverless.toml
gp open aws/aliases/serverless.toml
```

```toml
[toplevel]
<FILL IN NEW COMMMANDS>
```

```sh
./bin/aws-alias serverless
aws new-command
```

## Bash Scripts

```sh
[toplevel]
textalert =
  !f() {
    aws sns publish --message "${1}" --phone-number ${2}
  }; f
```

```sh
aws textalert $message $number
```