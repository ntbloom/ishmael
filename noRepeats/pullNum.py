# noRepeats.py
# makes funBook not repeat any paragraphs in its script

#!usr/bin/python3
import sqlite3, random


# connect to sqlite database
'''
dbFile = "./paragraphs.db"
conn = sqlite3.connect(dbFile)
cursor = conn.cursor()
'''

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

    '''
    possible = cursor.fetchall()          
    possible = [i[0] for i in possible]  # converts from tuple to list

    begin = possible[0]                     
    end = possible[-1]                     
    rand = random.randint(begin, end)     
    print('rand: ', rand)
    '''
    try:
        cursor.execute('INSERT INTO used (id) VALUES (?)', (rand[0],))
        cursor.execute('DELETE FROM master WHERE id=?', (rand[0],))
    except:
        print("all done!")
    # commit changes
    conn.commit()
    conn.close()

def debug():    
    ''' prints output of pullNum to terminal '''
    dbFile = "./paragraphs.db"
    conn = sqlite3.connect(dbFile)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * from used')
    used = cursor.fetchall()
    used = [i[0] for i in used]
    print('used:', used)
    cursor.execute('SELECT * from master')
    master = cursor.fetchall()
    master = [i[0] for i in master]
    print('master:', master)
    
    conn.close()

print('before')
debug()
pullNum()
print('\nafter')
debug()
