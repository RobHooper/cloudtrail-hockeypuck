#!/bin/bash
. ct-config

# Get how many messages are in the queue
X=`aws --profile "$AWSPROFILE" --region "$AWSREGION" --output text sqs get-queue-attributes --queue-url $AWSCTQUEUE --attribute-names ApproximateNumberOfMessages | cut -f '2'`

if (( "$X" > 0 )); then
  Y="$X"
else
  exit
fi
if (( "$X" > 5 )); then
  Y="5"
fi


echo "$Y"

for (( Z=1; Z<="$Y"; Z++ )) ; do
  echo "ran"
done
