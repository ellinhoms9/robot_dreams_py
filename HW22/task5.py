import sqlite3
from pprint import pprint

conn = sqlite3.connect("database_1.sqlite")
cursor = conn.cursor()

query = ("SELECT age, COUNT(id) AS users FROM users "
         "GROUP BY age HAVING users > 1 "
         "ORDER BY users DESC, age ")

res = cursor.execute(query)
pprint(res.fetchall())

# OR WE CAN MAKE IT LIKE THIS

# import sqlite3
# from pprint import pprint
#
# conn = sqlite3.connect("database_1.sqlite")
# cursor = conn.cursor()
#
# query = ("SELECT age, users FROM ("
#          "SELECT age, COUNT(id) AS users FROM users "
#          "GROUP BY age ORDER BY users DESC, age) "
#          "WHERE users > 1")
#
# res = cursor.execute(query)
# pprint(res.fetchall())
