import sqlite3
from pprint import pprint


conn = sqlite3.connect("book_store.sqlite")
cursor = conn.cursor()

query = ("SELECT purchase.id, purchase.date, users.first_name, users.last_name "
         "FROM purchase "
         "JOIN users ON users.id = purchase.user_id")


res = cursor.execute(query)
pprint(res.fetchall())
