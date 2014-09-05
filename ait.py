#!/usr/bin/env python

import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', nargs ='*')
args = parser.parse_args()

# Parses instance-ids out of describe-instances input.
command1 = ["jq", "-r", ".Reservations[].Instances[].InstanceId"]

# Basic xargs with a replacement string.
command2 = ["xargs", "-I", "%", "aws", "ec2", "create-tags", "--resources", "%", "--tags"]

# Prepare and append the command line key:value pairs for adding to the base command.
tags = ['Key=' + str(j[0]) + ',' + 'Value=' + str(j[1]) for j in [i.split(':') for i in args.t]] 
command2.extend(tags)

# Pipe everything together and print the result.
p1 = subprocess.Popen(command1, stdout=subprocess.PIPE)
p2 = subprocess.Popen(command2, stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output,err = p2.communicate()
print output
