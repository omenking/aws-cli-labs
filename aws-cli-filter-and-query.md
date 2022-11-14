## Filtering

AWS CLI allows you to filter server-side.

The command varies per service:
- --filters
- --filter
- --filter-expression

>  The service only returns matching results which can speed up HTTP response times for large data sets.


When using filters we need to always check the docs to see what we can filter by

https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpcs.html#options


```
aws ec2 describe-vpcs --filters "Name=is-default,Values=true"
```

## Querying

AWS CLI allows you to filter query-side.

> This parameter has capabilities the server-side filtering might not have.

```
aws ec2 describe-vpcs --query "Vpcs[0].CidrBlock"
```

## Examples
