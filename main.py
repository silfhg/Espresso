 import sqlite3
from sqlite3 import Error
w=12                      
database = "C:\\sqlite\pythonsqlite.db"
conn = sqlite3.connect(database)
cur = conn.cursor()
cur.execute("SELECT * FROM users")
col_name_list = [t[0] for t in cur.description]
print(*[s.ljust(w) for s in col_name_list])
print('-'*w*3)          
rows = cur.fetchall()
for row in rows:
        print(*[str(s).ljust(w) for s in row])
cur.close()
conn.close()
