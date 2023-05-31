import sqlite3
from pprint import pprint


conn = sqlite3.connect("book_store.sqlite")
cursor = conn.cursor()

query = ("SELECT books.title, COUNT(purchase.id) AS total "
         "FROM books "
         "JOIN purchase on purchase.book_id = books.id "
         "GROUP BY books.title "
         "ORDER BY total DESC "
         )

res = cursor.execute(query)
pprint(res.fetchall())
