import sqlite3
from pprint import pprint


conn = sqlite3.connect("book_store.sqlite")
cursor = conn.cursor()

query = ("SELECT COUNT(purchase.id) AS amount "
         "FROM purchase "
         "JOIN books ON books.id = purchase.book_id "
         "WHERE author = 'Rowling'"
         )

res = cursor.execute(query)
pprint(res.fetchall())
