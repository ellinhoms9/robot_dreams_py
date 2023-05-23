import sqlite3
connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

data = [
    ("Marian", "Smeryk", 26),
    ("Marta", "Smeryk", 22),
    ("Ivan","Laba", 20),
    ("Stepan", "Lega", 45),
    ("Nazar", "Semeniv", 56)
]

query = "INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)"

cursor.executemany(query, data)
connection.commit()
