## Chaining AWS CLI commands with XARGS for input


Image result for xargs -I
The xargs command builds and executes commands provided through the standard input. It takes the input and converts it into a command argument for another command.

```
VPC_ID=$(aws ec2 describe-vpcs --query "Vpcs[0].VpcId")
echo $VPC_ID
aws ec2 describe-subnets --filters="Name=vpc-id,Values=$VPC_ID" --query "Subnets[*].[CidrBlock,SubnetId]" --output table
```

```
aws ec2 run-instances \
    --image-id ami-1234 \
    --output text \
    --query Instances[*].[InstanceId] | \
xargs -I {} aws ec2 create-tags \
    --resources {} \
    --tags 'Key="foo",Value="bar"'
```