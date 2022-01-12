from dbConnect import *
def showRecords():
    cursor.execute('SELECT * FROM members')
    row = cursor.fetchall()
    for record in row:
        print(record)
showRecords()
