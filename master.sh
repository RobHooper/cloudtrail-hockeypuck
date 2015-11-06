#!/bin/bash
######################
# Master script that connects all other scripts and automates the process
###################
. ctconfig.py
######################################
set -euo pipefail
IFS=$'\n\t'
# Make temp directory in local dir
LOC=`mktemp -d CT-XXXXXX`

# Download an SQS message
aws --profile "$AWSPROFILE" --region "$AWSREGION" sqs receive-message --queue-url $AWSCTQUEUE > $LOC/SQS-Message

# Pull information out of the message
VAR=( $(./query-sqs.py $LOC/SQS-Message) )

#### Get info out of ^

# Download the file
aws --profile "$AWSPROFILE" s3 cp s3://${VAR[1]}/${VAR[2]} $LOC/

# Get file basename
CTFILE=`basename ${VAR[2]}`

# Get amount of entries in the data
LEN=`zcat $LOC/$CTFILE | ./jsonlen.py`

# Insert into mysql for each entry
for (( X=0; X<=$LEN-1; X++ )) ; do
  zcat $LOC/$CTFILE | ./query-ct.py $X
done

# remove sqs message
aws --profile "$AWSPROFILE" --region "$AWSREGION" sqs delete-message --queue-url $AWSCTQUEUE --receipt-handle ${VAR[0]}

# remove temporary file
rm -rf $LOC
