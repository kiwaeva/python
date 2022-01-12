from dbConnect import *
import time

def addMembers():
    #create an empty list members
    members = []
    #memberiD field is autoincrement 

    fname=input("Enter your first name: ")
    lname=input("Enter your last name: ")
    email=input("Enter your email: ")

    members.append(fname)
    members.append(lname)
    members.append(email)

    try:
        cursor.execute("INSERT INTO members VALUES (NULL,?,?,? )", members)
        conn.commit()
        print("Member Added")

        time.sleep(2)
        cursor.execute('SELECT * FROM members')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("record is not added")

# addMembers()
        

