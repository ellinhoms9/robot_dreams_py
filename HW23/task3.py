import sqlite3
from pprint import pprint


conn = sqlite3.connect("book_store.sqlite")
cursor = conn.cursor()

query = ("SELECT users.id, users.first_name, users.last_name, books.title "
         "FROM users "
         "JOIN purchase ON users.id = purchase.user_id "
         "JOIN books ON purchase.book_id = books.id "
         "ORDER BY users.id "
          )

res = cursor.execute(query)
pprint(res.fetchall())
