import sqlite3
import datetime
print(datetime.date.today())
print(type(datetime.date.day))
conn = sqlite3.connect('Test.db')

c = conn.cursor()

#c.execute("""CREATE TABLE employees (
#        date text,
#        infected integer
#        )""")
conn.commit()

conn.close()