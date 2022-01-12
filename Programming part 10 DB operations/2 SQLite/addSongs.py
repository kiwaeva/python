from myConnection import *
import time

# create a subroutine add members
def addSongs():
    # create an empty list members
    songs = []
    #memberID field is autoincrement
    # using the lastrowid property of the cursor object
    songID = cursor.lastrowid 
    print(songID)
    title = input("Enter song Title: ")
    artist = input("Enter Artist name: ")
    genre = input("Enter song Genre: ")

    songs.append(songID)
    songs.append(title)
    songs.append(artist)
    songs.append(genre)
    


    try:
        cursor.execute('INSERT INTO songs VALUES (?,?,?,?)', songs)
        conn.commit()
        print("Song Added")

        time.sleep(3)
        cursor.execute('SELECT * FROM songs')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("record not added")

addSongs()      


