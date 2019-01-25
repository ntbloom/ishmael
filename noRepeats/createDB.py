# createDB.py
# creates sqlite database for noRepeats part of funBook

#!usr/bin/python3
import sqlite3

# connect to sqlite database

dbFile = "./paragraphs.db"
conn = sqlite3.connect(dbFile)
cursor = conn.cursor()


# define upper and lower limits for paragraphs, dump into a list

first = 63    #opening paragraph should be 63 in deployment
last = 90     #closing paragraph should be 2964 in deployment
array = []
for i in range(last-first+1):
    i = first
    array.append(i)
    first += 1

#create the master table from scratch -- uncomment to start over
cursor.execute('DELETE FROM master')
cursor.execute('DELETE from used')
for i in range(len(array)):
    cursor.execute('INSERT INTO master (id) VALUES (?)', (array[i],))
conn.commit()
