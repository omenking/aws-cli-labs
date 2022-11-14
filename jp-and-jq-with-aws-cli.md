## JP and JQ with AWS CLI

## What is JQ?

Its a command line tool used to parse, format or transform JSON respones from other commands

https://stedolan.github.io/jq/manual/
https://cheatography.com/orabig/cheat-sheets/jq/

## What is JP?

Its similar to JQ but suppose to be easier to use since it uses JMESPath syntax.

https://github.com/jmespath/jp
https://jmespath.org/

## Sample

Sample JSON from `aws ec2 describe-vpcs`

```json
{
    "Vpcs": [
        {
            "CidrBlock": "192.168.100.0/22",
            "DhcpOptionsId": "dopt-ddeb2aa6",
            "State": "available",
            "VpcId": "vpc-062b7eef861746a7d",
            "OwnerId": "655604346524",
            "InstanceTenancy": "default",
            "CidrBlockAssociationSet": [
                {
                    "AssociationId": "vpc-cidr-assoc-033eddfe5c93b5765",
                    "CidrBlock": "192.168.100.0/22",
                    "CidrBlockState": {
                        "State": "associated"
                    }
                }
            ],
            "IsDefault": false,
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "exampro-accounts"
                }
```

## JQ Examples

```
sudo apt-get install jq
```

```
aws ec2 describe-vpcs | jq .
aws ec2 describe-vpcs | jq .Vpcs
aws ec2 describe-vpcs | jq Vpcs
aws ec2 describe-vpcs | jq .Vpcs[]
aws ec2 describe-vpcs | jq .Vpcs.CidrBlock
aws ec2 describe-vpcs | jq .Vpcs?.CidrBlock?
aws ec2 describe-vpcs | jq .Vpcs[].CidrBlock
aws ec2 describe-vpcs | jq .Vpcs[1].CidrBlock
aws ec2 describe-vpcs | jq .Vpcs[1:2].CidrBlock
aws ec2 describe-vpcs | jq .Vpcs[1:2]
aws ec2 describe-vpcs | jq .Vpcs[1:1]
aws ec2 describe-vpcs | jq .Vpcs[1:2][].CidrBlock
aws ec2 describe-vpcs | jq .Vpcs[1,2]
aws ec2 describe-vpcs | jq .Vpcs[1,2].CidrBlock
aws ec2 describe-vpcs | jq .Vpcs[1].CidrBlock,.Vpcs[1].VpcId
aws ec2 describe-vpcs | jq .Vpcs[1,2].CidrBlock,.Vpcs[1,2].VpcId
aws ec2 describe-vpcs | jq .Vpcs[1].CidrBlock|.Vpcs[1].VpcId
aws ec2 describe-vpcs | jq ".Vpcs[] | .CidrBlock"
aws ec2 describe-vpcs | jq '.Vpcs[] | .CidrBlock'
aws ec2 describe-vpcs | jq '.Vpcs[] | .CidrBlock,.VpcId'
aws ec2 describe-vpcs | jq '{cidr: Vpcs[].CidrBlock, id: Vpcs[].CidrBlock }'
aws ec2 describe-vpcs | jq '{cidr: .Vpcs[0].CidrBlock, id: .Vpcs[0].VpcId }'
aws ec2 describe-vpcs | jq '{cidr: .Vpcs[0,1].CidrBlock, id: .Vpcs[0,1].VpcId }'
aws ec2 describe-vpcs | jq '{cidr: .Vpcs[0,1].CidrBlock, id: .Vpcs[0,1].VpcId }'
jq {hello: 'world'}
aws ec2 describe-vpcs | jq '.Vpcs[0,1] | {CidrBlock,VpcId}'
aws ec2 describe-vpcs | jq '.Vpcs[0,1] | {cidr: CidrBlock, id: VpcId}'
aws ec2 describe-vpcs | jq '.Vpcs[0,1] | {cidr: .CidrBlock, id: .VpcId}'
export USERNAME='andrewbrown'
export PASSWORD='testing123'
jq --null-input \
  --arg user "$USERNAME" \
  --arg password "$PASSWORD" \
  '{"user": $user, "password": $password}'
jq --null-input \
  --arg user "$USERNAME" \
  --arg password "$PASSWORD" \
  '{"user": $user, "password": $password}' > creds.json
cat creds.json
```

### JP Examples

```
npm i jp -g
```

```
aws ec2 describe-vpcs | jp .
aws ec2 describe-vpcs | jp .Vpcs
aws ec2 describe-vpcs | jp Vpcs
aws ec2 describe-vpcs | jp Vpcs[*].CidrBlock
```

## Conclusion

- JQ and JP are very similar.
- JQ appears more robust, prints nicer
- JP syntax does not appear much easier
- JP