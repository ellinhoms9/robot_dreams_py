import sqlite3
from pprint import pprint

conn = sqlite3.connect("database_1.sqlite")
cursor = conn.cursor()

query = "SELECT age, COUNT(id) AS users FROM users GROUP BY age"

res = cursor.execute(query)
pprint(res.fetchall())
