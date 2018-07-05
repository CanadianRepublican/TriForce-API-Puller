# requirement: python-mysqldb

import MySQLdb as dbapi
import sys
import csv
import time

timestr = time.strftime("%Y%m%d")

QUERY='SELECT * FROM mydb.people;'
db=dbapi.connect(host='localhost',user='root',passwd='password')

cur=db.cursor()
cur.execute(QUERY)
result=cur.fetchall()

c = csv.writer(open('daily-csv-export-'+timestr+'.csv', 'wb'))
for x in result:
c.writerow(x)
