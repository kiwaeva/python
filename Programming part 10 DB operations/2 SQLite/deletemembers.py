from myConnection import *

#create or open a database called c2Music.db
conn = sqlite3.connect('c2Music.db')
cursor = conn.cursor()

def delRecord():
    keyField=input("Enter ID of the record to be deleted: ")
    try:
        cursor.execute("DELETE FROM members WHERE MemberID= "+ keyField)
        conn.commit()
        print("\Record deleted")

        time.sleep(2)
        cursor.execute('SELECT * FROM members')
        row=cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Record is not deleted")


def showRecords():
    searchID= input("Enter ID of record to search for: ")
    cursor.execute('SELECT * FROM members WHERE MemberID=' + searchID)
    row = cursor.fetchall()
    for record in row:
        print(record)


# showRecords()
# delRecord()