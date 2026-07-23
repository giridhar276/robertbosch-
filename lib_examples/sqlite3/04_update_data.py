import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))
conn.commit()
print("Rows updated:", cursor.rowcount)
conn.close()
