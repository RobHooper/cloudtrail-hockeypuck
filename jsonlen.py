#!/usr/bin/python2.7
##
# Get how many json messages are in the file
# There is a record in 0 which will make the total +1 more than the last record location
##
import json, sys
x = json.load(sys.stdin)
print len(x['Records'])
