# noRepeats.py
# makes funBook not repeat any paragraphs in its script

#!usr/bin/python3
import sqlite3, datetime
from createDB import createDB


class Randpop:
    def __init__(self, database='./paragraphs.db', first=63, last=70):
        self.database = database
        self.first = first  # paragraph number to start
        self.last = last    # paragraph number to finish 
        self.conn = sqlite3.connect(self.database) #used to commit/close
        self.cursor = self.conn.cursor() #used for SQL queries

    def pullNum(self):
        '''pops random number from master, adds to used'''
        try:    # until all paragraphs run out
            
            # pull random number from master
            self.cursor.execute('SELECT * from master ORDER BY RANDOM() LIMIT 1') 
            rand = self.cursor.fetchall() 
           
           
            rand = [i[0]for i in rand]
            print('rand: ', rand)
        
            # pops from 'master', pushes to 'used' with date stamp
            date = datetime.datetime.now() 
            self.cursor.execute('INSERT INTO used (id, day, month, year) \
                VALUES (?,?,?,?)', [rand[0], date.day, date.month, date.year])
            self.cursor.execute('DELETE FROM master WHERE id=?', (rand[0],))
            # commit changes
            self.conn.commit()

        except:
            # start all over again
            self.createDB()
            self.pullNum()

    
    def createDB(self):
        '''creates database with list according to Moby Dick paragraphs'''
        
        # create tables
        
        self.cursor.execute('DROP TABLE IF EXISTS master')
        self.cursor.execute('CREATE TABLE master (id integer)')
        self.cursor.execute('DROP TABLE IF EXISTS used')
        self.cursor.execute('CREATE TABLE used \
            (id integer, month integer, day integer, year integer)')

        # define upper and lower limits for paragraphs, dump into a list
        
        array = []
        for i in range(self.last-self.first+1):
            i = self.first
            array.append(i)
            self.first += 1


        # populates master table

        self.cursor.execute('DELETE FROM master')
        self.cursor.execute('DELETE from used')
        for i in range(len(array)):
            self.cursor.execute('INSERT INTO master (id) VALUES (?)', (array[i],))
        self.conn.commit()

    def debug(self):    
        ''' prints output of pullNum to terminal for development/debugging'''
        self.cursor.execute('SELECT * from used')
        used = self.cursor.fetchall()
        print('used:\n', used)
        
        self.cursor.execute('SELECT * from master')
        master = self.cursor.fetchall()
        master = [i[0] for i in master]
        print('master:', master)
