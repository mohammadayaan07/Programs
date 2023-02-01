#thirdbd.py
import mysql.connector
bad=mysql.connector.connect(host="localhost",
							user="root",
							passwd="ERROR",
							database="thirdbd")
cm=bad.cursor()
s="CREATE TABLE book11 (bookid integer(4),title varchar(20),price float(5,2),pin integer(6),phonenu integer(11))"
cm.execute(s)