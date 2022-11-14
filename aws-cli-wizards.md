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