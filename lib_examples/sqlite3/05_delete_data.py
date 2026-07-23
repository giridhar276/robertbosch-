import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM users WHERE name = ?", ("Bob",))
conn.commit()
print("Rows deleted:", cursor.rowcount)
conn.close()
