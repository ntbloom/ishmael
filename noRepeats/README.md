### build instructions for noRepeats

Script is dependent on paragraphs.db file for execution

```
touch paragraphs.db
```

Remaining methods are contained in Randpop.py


```python
from Randpop import Randpop

randpop = Randpop()     # inits class
randpop.createDB()      # populates sqlite database files
randpop.pullNum()       # pulls random number, records transaction
```

Note that createDB() erases existing data and begins recounting from
beginning
