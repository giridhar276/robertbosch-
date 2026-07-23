import sqlite3
with sqlite3.connect("app.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    print("Total users:", cursor.fetchone()[0])
