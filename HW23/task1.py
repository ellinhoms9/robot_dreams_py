import sqlite3
conn = sqlite3.connect("books_db_new.sqlite")
cursor = conn.cursor()

table_users = ("CREATE TABLE IF NOT EXISTS users ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "first_name TEXT,"
               "last_name TEXT,"
               "age INTEGER NOT NULL)"
               )


table_publishing_house = ("CREATE TABLE IF NOT EXISTS publishing_house ("
                          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                          "name TEXT,"
                          "rating INTEGER DEFAULT 5)"
                          )


table_books = ("CREATE TABLE IF NOT EXISTS books ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "title TEXT,"
               "author TEXT,"
               "year INTEGER NOT NULL,"
               "price INTEGER NOT NULL,"
               "publishing_house_id INTEGER NOT NULL,"
               "FOREIGN KEY (publishing_house_id) REFERENCES publishing_house(id))"
               )


table_purchases = ("CREATE TABLE IF NOT EXISTS purchases ("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "user_id INTEGER NOT NULL,"
                   "book_id INTEGER NOT NULL,"
                   "date TEXT DEFAULT CURRENT_TIMESTAMP,"
                   "FOREIGN KEY (user_id) REFERENCES users(id),"
                   "FOREIGN KEY (book_id) REFERENCES books(id))"
                   )

cursor.execute(table_users)
cursor.execute(table_publishing_house)
cursor.execute(table_books)
cursor.execute(table_purchases)
