#!/usr/bin/python2.7
##########################################
# Query the cloudtrail data so that we can seperate out the different records.
#
############### Editable variables ######
from ctconfig import *
##############

import json, sys

X = json.load(sys.stdin)
X = X['Records'][int(sys.argv[1])]

####### Python connect to mysql
import MySQLdb

db = MySQLdb.connect(host=hostname,
                     user=username,
                     passwd=password,
                     db=database,)
cursor = db.cursor()

XUI=json.dumps(X['userIdentity'])

VARNAME="eventVersion, eventID, eventTime, eventType, awsRegion, eventName, userIdentity, eventSource, sourceIPAddress, recipientAccountId"

VALUES="'"+X['eventVersion']+"','"+X['eventID']+"','"+X['eventTime']+"','"+X['eventType']+"','"+X['awsRegion']+"','"+X['eventName']+"','"+XUI+"','"+X['eventSource']+"','"+X['sourceIPAddress']+"','"+X['recipientAccountId']+"'"

# Test that the event is not in there previously
SAN = cursor.execute("SELECT eventID FROM %s where eventID = '%s'" % (tablename, X['eventID']))
if SAN == 0 :
    cursor.execute("INSERT INTO %s (%s) VALUES (%s);" % (tablename, VARNAME, VALUES))

db.commit()

# close the cursor object
cursor.close ()

# close the connection
db.close ()
