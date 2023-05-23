import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

query = ("CREATE TABLE users ("
         "id INTEGER PRIMARY KEY AUTOINCREMENT,"
         "first_name TEXT NOT NULL UNIQUE ,"
         "last_name TEXT NOT NULL UNIQUE ,"
         "age INTEGER)")


cursor.execute(query)
