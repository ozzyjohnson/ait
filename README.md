ait
===

A quick script I threw together to simplify tagging AWS instances when using the AWS CLI.

It takes input piped from ```aws ec2 describe-instances``` and uses a single switch to specify a list of key:value pairs to add.

**Example:**

```aws ec2 describe-instances --filter Name=tag-value,Values=web | ait.py -t group:alpha cluster:database node:4```

**Requires:**

* [jq](http://stedolan.github.io/jq/)
* [xargs](http://linux.die.net/man/1/xargs)

**To-do:**

* Pretty naive, is there a better way to string this together?
* Handle (detect) other resource types.
* Tag deletion.
* Error handling.
* Usage.

