import mysql.connector

conn = mysql.connector.connect(host = "localhost", database="swimming_lessons", user = "root", password="Bubucite123!")

if conn.is_connected():
    print("Connected to MySQL")
else:
    print("connection failed")

cursor=conn.cursor(prepared=True)
