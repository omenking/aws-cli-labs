## Chaining AWS CLI commands with XARGS for input


Image result for xargs -I
The xargs command builds and executes commands provided through the standard input. It takes the input and converts it into a command argument for another command.

aws ec2 describe-vpcs --query "Vpcs[0].VpcId"

```
aws ec2 run-instances \
    --image-id ami-1234 \
    --output text \
    --query Instances[*].[InstanceId] | \
xargs -I {} aws ec2 create-tags \
    --resources {} \
    --tags 'Key="foo",Value="bar"'
```