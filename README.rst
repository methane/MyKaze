=======
MyKaze
=======

MyKaze is [Motor](https://github.com/mongodb/motor/) like bridge between
Tornado and PyMySQL.

You can access to MySQL from tornado without
[background thread](https://gist.github.com/methane/2185380) like this:

```python
import mykaze
from mykaze.util import wrap_green

@wrap_green
def fetch_sleep():
    con = mykaze.connect(...)
    cur = con.cursor()
    cur.execute("SELECT SLEEP(3)")
    return cur.fetchone()
```

Hint: SQLAlchemy's engine accepts `creator` argument.

```python
engine = create_engine('mysql+pymysql://', creator=lambda: mykaze.connect(...))
```

This package is in Proof of Concept status.
After PyMySQL has pluggable stream, MyKaze will be a plugin.
