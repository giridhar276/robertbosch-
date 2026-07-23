import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
try:
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Frank", 40))
    raise ValueError("Simulated error before commit")
    conn.commit()
except ValueError as e:
    conn.rollback()
    print("Rolled back due to:", e)
conn.close()
