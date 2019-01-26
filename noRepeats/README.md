# Randpop
-Pops random numbers from sqlite table and pushes into another

-Records the difference with a time stamp

</br>

### build instructions

Script is dependent on paragraphs.db file for execution

```
touch paragraphs.db
```

</br>

Remaining methods are contained in Randpop.py


```python
from Randpop import Randpop

randpop = Randpop()     # inits class
randpop.createDB()      # populates sqlite database files
randpop.pullNum()       # pulls random number, records transaction
randpop.debug()         # prints 'master' and 'used' tables to terminal
```

Note that ```createDB()``` erases existing data and begins recounting from beginning. Should only be invoked once, at initial deployment.
