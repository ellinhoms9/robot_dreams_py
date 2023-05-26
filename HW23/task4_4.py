import sqlite3
from pprint import pprint


conn = sqlite3.connect("book_store.sqlite")
cursor = conn.cursor()

query = ("SELECT books.author, SUM(books.price), COUNT(purchase.id) "
         "FROM books "
         "JOIN purchase ON books.id = purchase.book_id "
         "GROUP BY books.author "
         )

res = cursor.execute(query)
pprint(res.fetchall())
