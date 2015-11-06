#!/usr/bin/python2.7

### Usage
# ./query-sqs.py dir/sqs-message.json
##
# Use SQS JSON and use it to download the S3 file it is pointing to
# SQS JSON is in the sqs-message.json
####

import json, sys

# FileName set when script is called
FN = sys.argv[1]

# Open file and load data
with open(FN) as data_file:
	data = json.load(data_file)

# Get SQS data
sqsdata = json.loads(data['Messages'][0]['Body'])

# Get original message
#message = json.loads(sqsdata['Message'])

# Print message details
#Message key
print data['Messages'][0]['ReceiptHandle']
# Bucket name
print sqsdata['Records'][0]['s3']['bucket']['name']
# File details
print sqsdata['Records'][0]['s3']['object']['key']
