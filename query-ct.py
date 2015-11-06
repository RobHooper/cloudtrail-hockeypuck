#!/usr/bin/python2.7
##########################################
# Query the cloudtrail data so that we can seperate out the different records.
#
############### Editable variables ######
hostname = ""
username = ""
password = ""
database = ""
tablename = ""
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
cursor.execute("INSERT INTO",tablename,"(eventVersion, eventID, eventTime, eventType, awsRegion, eventName, userIdentity, eventSource, sourceIPAddress, recipientAccountId)VALUES ('"+X['eventVersion']+"','"+X['eventID']+"','"+X['eventTime']+"','"+X['eventType']+"','"+X['awsRegion']+"','"+X['eventName']+"','"+json.dumps(X['userIdentity'])+"','"+X['eventSource']+"','"+X['sourceIPAddress']+"','"+X['recipientAccountId']+"');")
db.commit()

# close the cursor object
cursor.close ()

# close the connection
db.close ()
