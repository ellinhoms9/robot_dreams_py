import sqlite3
from pprint import pprint


conn = sqlite3.connect("book_store.sqlite")
cursor = conn.cursor()

query = ("SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases "
         "FROM users "
         "JOIN purchase ON users.id = purchase.user_id "
         "JOIN books ON purchase.book_id = books.id "
         "GROUP BY users.id "
         )

res = cursor.execute(query)
pprint(res.fetchall())
