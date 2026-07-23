import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
conn.commit()
print("Inserted rows")
conn.close()
