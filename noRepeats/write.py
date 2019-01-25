# noRepeats.py
# makes funBook not repeat any paragraphs in its script

#!usr/bin/python3
import sqlite3

# connect to sqlite database
dbFile = "./paragraphs.db"
conn = sqlite3.connect(dbFile)
cursor = conn.cursor()

# define upper and lower limits for paragraphs, dump into a list
first = 63      #opening paragraph
last = 2964     #closing paragraph
array = []
for i in range(last-first+1):
    i = first
    array.append(i)
    first += 1

##create the master table from scratch -- uncomment to start over
##for i in range(len(array)):
##    cursor.execute('INSERT INTO master (id) VALUES (?)', (array[i],))
##conn.commit()
