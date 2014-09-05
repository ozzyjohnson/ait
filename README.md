ait
===

A quick script to simplify tagging AWS instances. Takes input piped from the aws ec2 describe-instances.

**Requires:**

* jq
* xargs

**Example:**

```aws ec2 describe-instances --filter Name=tag-value,Values=web | ait.py -t group:alpha cluster:database node:4```

**To-do:**

* Pretty naive, is there a better way to string this together?
* Handle other resource types.
