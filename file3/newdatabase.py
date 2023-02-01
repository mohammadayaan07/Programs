#newdatabase.py
import mysql.connector

mydb=mysql.connector.connect(host="localhost",
							user="root",
							passwd="ERROR",
							database="mydb")
cur=mydb.cursor()
s="CREATE TABLE MYBD (name varchar(20),class int(4),rollno float(5,3))"
cur.execute(s)