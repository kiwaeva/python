from myConnection import *

def update():
    #enter id of the record to be updated
    keyField = input("Enter the ID of the record to be updated:")
    #enter the field name to be updated
    field = input("Which field do you want to update:(Firstname, Lastname,Email)")
    newFieldValue = input ("Enter the new value: ")
    print(newFieldValue)
    #Update members set fieldname = 'fieldValue'
    newFieldValue= "'" + newFieldValue + "'"
    print(newFieldValue)

    try:
        # field = Firstname, Lastname,Email and value = newFieldValue, where memberID = number
        cursor.execute("UPDATE members SET " + field + "=" + newFieldValue + "WHERE MemberID=" + keyField)
        conn.commit()
        print("Member Updated")

        time.sleep(2)
        cursor.execute('SELECT * FROM members')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Record is not updated")
# update()
