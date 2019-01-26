#!usr/bin/python3
#
# testing.py, script for testing pullNum class

from pullNum import Randpop

random = Randpop()

random.createDB()
for i in range(25):
    random.pullNum()
    random.debug()
