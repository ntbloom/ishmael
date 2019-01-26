# Randpop.py
# 
# mimicks a pop/push stack in sqlite for pulling random numbers and
# recording each iteration
#
# used to make funBook not repeat any paragraphs in its script

#!usr/bin/python3
import sqlite3, datetime
from createDB import createDB


class Randpop:
    def __init__(self, database='./paragraphs.db', first=63, last=2964):
        self.database = database
        self.first = first  # paragraph number to start
        self.last = last    # paragraph number to finish 
        self.conn = sqlite3.connect(self.database) #used to commit/close
        self.cursor = self.conn.cursor() #used for SQL queries

    def pullNum(self):
        '''pops random number from master, adds to used'''
        # checks master to see if there are still numbers available
        self.cursor.execute('SELECT * from master')
        test = self.cursor.fetchall()
        
        # pull random number from master
        self.cursor.execute('SELECT * from master ORDER BY RANDOM() LIMIT 1') 
        rand = self.cursor.fetchall()
        rand = [i[0]for i in rand] # converts from tuple to list
    
        # pops from 'master', pushes to 'used' with date stamp
        date = datetime.datetime.now() 
        self.cursor.execute('INSERT INTO used (id, day, month, year) \
            VALUES (?,?,?,?)', [rand[0], date.day, date.month, date.year])
        self.cursor.execute('DELETE FROM master WHERE id=?', (rand[0],))
        
        # commit changes
        self.conn.commit()

        # restarts database if it runs out of numbers
        if len(test) == 1:
            self.createDB()
            #TODO: add anything else you want to happen when book ends
    
    def createDB(self):
        '''creates database with list starting at first, ending at last'''
        
        # create tables
        self.cursor.execute('DROP TABLE IF EXISTS master')
        self.cursor.execute('CREATE TABLE master (id integer)')
        self.cursor.execute('DROP TABLE IF EXISTS used')
        self.cursor.execute('CREATE TABLE used \
            (id integer, month integer, day integer, year integer)')

        # define upper and lower limits for paragraphs, dump into a list
        array = []
        first = self.first
        last = self.last
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

    def debug(self):    
        ''' prints output of pullNum to terminal for development/debugging'''
        self.cursor.execute('SELECT * from used')
        used = self.cursor.fetchall()
        print('used:\n', used)
        self.cursor.execute('SELECT * from master')
        master = self.cursor.fetchall()
        master = [i[0] for i in master]
        print('master:', master)
