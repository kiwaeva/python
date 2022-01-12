from myConnection import *
import time


# keyfield = keyfield + keyfield
def delSong():
    keyField=input("Enter ID of song to be delted: ")
    try:
        cursor.execute("DELETE FROM songs WHERE SongID=" + keyField)
        conn.commit()
        print("\Record deleted")

        time.sleep(2)
        cursor.execute('SELECT * FROM songs')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Record not deleted")


def searchSongs():
    songID = input("Enter ID of songs to search for: ")

    cursor.execute('SELECT * FROM songs WHERE SongID='+ songID)
    row = cursor.fetchall()
    for record in row:
        print(record)


searchSongs()
delSong()
