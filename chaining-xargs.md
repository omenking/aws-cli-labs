## Chaining AWS CLI commands with XARGS for input

```
aws ec2 run-instances \
    --image-id ami-1234 \
    --output text \
    --query Instances[*].[InstanceId] | \
xargs -I {} aws ec2 create-tags \
    --resources {} \
    --tags 'Key="foo",Value="bar"'
```