# noRepeats.py
# makes funBook not repeat any paragraphs in its script

#!usr/bin/python3
import sqlite3, datetime
from createDB import createDB


def pullNum():
    '''pops random number from master, adds to used'''
    # open database
    dbFile = "./paragraphs.db"
    conn = sqlite3.connect(dbFile)
    cursor = conn.cursor()

    # pull random number from master
    cursor.execute('SELECT * from master ORDER BY RANDOM() LIMIT 1') 
    rand = cursor.fetchall() 
    rand = [i[0]for i in rand]
    print('rand: ', rand)
    
    try:    # until all paragraphs run out
        date = datetime.datetime.now() 
        cursor.execute('INSERT INTO used (id, day, month, year) \
            VALUES (?,?,?,?)', [rand[0], date.day, date.month, date.year])
        cursor.execute('DELETE FROM master WHERE id=?', (rand[0],))
        # commit changes
        conn.commit()
        conn.close()

    except:
        # start all over again
        createDB()
        pullNum()

def debug():    
    ''' prints output of pullNum to terminal for development/debugging'''
    dbFile = "./paragraphs.db"
    conn = sqlite3.connect(dbFile)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * from used')
    used = cursor.fetchall()
    print('used:\n', used)
    
    cursor.execute('SELECT * from master')
    master = cursor.fetchall()
    master = [i[0] for i in master]
    print('master:', master)
    
    conn.close()

pullNum()
debug()
