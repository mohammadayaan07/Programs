#c
import mysql.connector
mybd=mysql.connector.connect(host="localhost",
user="root",
passwd="EEROR",
database="ayaanbd"
)
cur=mybd.cursor()
s="INSERT INTO book (BOOKID,TITLE,PRICE) VALUES(%s,%s%,s)"
b1=(1,"python",345)
cur.execute(s,b1)
mybd.commit()
