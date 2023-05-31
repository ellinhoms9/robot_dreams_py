import sqlite3
from pprint import pprint


conn = sqlite3.connect("book_store.sqlite")
cursor = conn.cursor()

query = ("SELECT users.id, COUNT(purchase.id) AS purchases_count "
         "FROM users "
         "JOIN purchase ON users.id = purchase.user_id "
         "GROUP BY users.id "
         )

res = cursor.execute(query)
pprint(res.fetchall())
