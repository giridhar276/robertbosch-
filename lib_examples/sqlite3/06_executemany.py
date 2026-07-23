import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
data = [("Charlie", 22), ("Dana", 28), ("Eve", 35)]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", data)
conn.commit()
print("Multiple rows inserted")
conn.close()
