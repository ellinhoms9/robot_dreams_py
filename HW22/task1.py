import sqlite3
from pprint import pprint

conn = sqlite3.connect("database_1.sqlite")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE age > 30"

res = cursor.execute(query)
pprint(res.fetchall())
