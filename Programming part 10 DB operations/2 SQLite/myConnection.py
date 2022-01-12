import sqlite3
import time
#create or open a database called c2Music.db
conn = sqlite3.connect('c2Music.db')
cursor = conn.cursor()