#cursor.py
import mysql.connector
mydb=mysql.connector.connect(host="localhost",
							user="root",
							passwd="ERROR",
							database="ayaanbd")
cm=mydb.cursor()
s="CREATE TABLE book (bookid integer(4),title varchar(20),price float(5,2))"
cm.execute(s)