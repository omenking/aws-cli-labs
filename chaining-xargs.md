## Chaining AWS CLI commands with XARGS for input


Image result for xargs -I
The xargs command builds and executes commands provided through the standard input. It takes the input and converts it into a command argument for another command.

## Storing the results as an Env Var
```
VPC_ID=$(aws ec2 describe-vpcs --query "Vpcs[0].VpcId") --output text
echo $VPC_ID
aws ec2 describe-subnets \
    --filters="Name=vpc-id,Values=$VPC_ID" \
    --query "Subnets[*].[CidrBlock,SubnetId]" \
    --output table
```

# Chaining commands using xargs
```
aws ec2 describe-vpcs --query "Vpcs[0].VpcId" --output text | \
xargs -I {} aws ec2 describe-subnets \
    --filters="Name=vpc-id,Values={}" \
    --query "Subnets[*].[CidrBlock,SubnetId]" \
    --output table
```