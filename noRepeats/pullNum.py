# noRepeats.py
# makes funBook not repeat any paragraphs in its script

#!usr/bin/python3
import sqlite3, datetime
from createDB import createDB

#file is

class Randpop:
    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(self.database) #used to commit/close
        self.cursor = conn.cursor() #used for SQL queries

    def pullNum(self):
        '''pops random number from master, adds to used'''
        # pull random number from master
        self.cursor.execute('SELECT * from master ORDER BY RANDOM() LIMIT 1') 
        rand = cursor.fetchall() 
        rand = [i[0]for i in rand]
        print('rand: ', rand)
        
        try:    # until all paragraphs run out
            date = datetime.datetime.now() 
            self.cursor.execute('INSERT INTO used (id, day, month, year) \
                VALUES (?,?,?,?)', [rand[0], date.day, date.month, date.year])
            self.cursor.execute('DELETE FROM master WHERE id=?', (rand[0],))
            # commit changes
            self.conn.commit()
            self.conn.close()

        except:
            # start all over again
            createDB()
            pullNum()

    
    def createDB(self):
        '''creates database with list according to Moby Dick paragraphs'''
        
        # create tables
        
        self.cursor.execute('DROP TABLE IF EXISTS master')
        self.cursor.execute('CREATE TABLE master (id integer)')
        self.cursor.execute('DROP TABLE IF EXISTS used')
        self.cursor.execute('CREATE TABLE used \
            (id integer, month integer, day integer, year integer)')


        # define upper and lower limits for paragraphs, dump into a list
        
        first = 63    #opening paragraph should be 63 in deployment
        last = 2964   #closing paragraph should be 2964 in deployment
        array = []
        for i in range(last-first+1):
            i = first
            array.append(i)
            first += 1


        # populates master table

        self.cursor.execute('DELETE FROM master')
        self.cursor.execute('DELETE from used')
        for i in range(len(array)):
            self.cursor.execute('INSERT INTO master (id) VALUES (?)', (array[i],))
        self.conn.commit()
        self.conn.close()

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
