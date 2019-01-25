# noRepeats.py
# makes funBook not repeat any paragraphs in its script

#!usr/bin/python3
import sqlite3, random


# connect to sqlite database

dbFile = "./paragraphs.db"
conn = sqlite3.connect(dbFile)
cursor = conn.cursor()

def pullNum():
    '''pops random number from master, adds to used'''
    cursor.execute('SELECT * from master')
    possible = cursor.fetchall()
    conn.commit()
    possible = [i[0] for i in possible]
    begin = possible[0]
    end = possible[-1]
    rand = random.randint(begin, end)
    print('rand: ', rand)

    cursor.execute('INSERT INTO used (id) VALUES (?)', (rand,))
    conn.commit()
    cursor.execute('DELETE FROM master WHERE id=?', (rand,))
    conn.commit()

    #debug
    cursor.execute('SELECT * from used')
    used = cursor.fetchall()
    conn.commit()
    used = [i[0] for i in used]
    print('used:', used)
    cursor.execute('SELECT * from master')
    master = cursor.fetchall()
    conn.commit()
    master = [i[0] for i in master]
    print('master:', master)
    conn.close()

pullNum()
