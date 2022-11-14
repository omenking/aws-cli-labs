# AWS CLI Autoprompt

## What is AWS CLI Autoprompt?

AWS CLI Autoprompt is an Interactive CLI which will provide contextual information as you type such as documentation, preview of output, and autcompletion.

## Configuration

Use the following flag:

```sh
aws --cli-auto-prompt
```

or keep it on wit this env var:

```sh
export AWS_CLI_AUTO_PROMPT=on-partial
```

 > Partial mode is recommended since full mode will prompt everytime, full mode can be annoying if you are copying and pasting full commands or you have a command already written.

## Tab autcompletion

- We can autcomplete what we are writing by pressing `<Tab>`
- We can navigate suggested completion search terms with the arrow keys

try to autcomplete:

```sh
aws ec2 --run-in<TAB>
```

## Required Fields

- We can easily see all possible fields, just type `--`
- You can see in the completion search terms which fields are required

try and see which fields are required:

```sh
aws dynamodb create-table --<TAB>
```

## Viewing Documentation

- Pressing [F3] will bring up a documentation pane
- As we type and add subcommands the documentation will contextually change
- We can navigate the docs by toggle panes by pressing [F2]

Turn on Docments pane and start type commands and subcommands:

```sh
aws s3 ls
```

## Resource Completion

- Sometimes fields with suggest resource completion

Try typing the following:
```
aws dynamodb describe-table --table-name
```

## History

Type `Ctrl+R` to bring up history of older commands.


## Outputted Structure

- Pressing [F5] will toggle out output pane
- We can observe what our outputted structure will work like
- Its not the actual data, its just skeleton structure of the output
- This doesn't work with filters and queries

```sh
aws ec2 describe-vpcs
```