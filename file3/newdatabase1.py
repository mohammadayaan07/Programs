#c
import mysql.connector
db=mysql.connector.connect(host="localhost",
						user="root",
						passwd="ERROR")
mb=db.cursor()
mb.execute("CREATE DATABASE ayaanbd")