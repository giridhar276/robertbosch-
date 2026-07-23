import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
conn.commit()
print("Table created")
conn.close()
