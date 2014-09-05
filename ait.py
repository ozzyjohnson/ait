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

# Make a list of lists out of the k:v pairs on the command line.
kvPairs = []
for kvPair in args.t:
        kvPairs.append(kvPair.split(':'))

# Append to the xargs command.
for pair in kvPairs:
    command2.append('Key=' + str(pair[0]) + ',' + 'Value=' + str(pair[1]))

# Pipe everything together and print the result.
p1 = subprocess.Popen(command1, stdout=subprocess.PIPE)
p2 = subprocess.Popen(command2, stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output,err = p2.communicate()
print output
