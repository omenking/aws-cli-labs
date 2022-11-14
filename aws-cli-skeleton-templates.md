

Another way we can configure AWS CLI fields is by provide either a json or yaml file.

```sh
aws ec2 run-instances --cli-input-json file://data.json
aws ec2 run-instances --cli-input-yaml file://data.yaml
```

# Dump YAMl
To get the structure we can

```sh
mkdir -p aws/cli/data
aws ec2 run-instances --generate-cli-skeleton yaml-input > aws/cli/data/new-instance.yaml  
```