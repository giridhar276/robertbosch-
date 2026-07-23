import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE temp_data (id INTEGER, value TEXT)")
cursor.execute("INSERT INTO temp_data VALUES (1, 'temporary')")
cursor.execute("SELECT * FROM temp_data")
print(cursor.fetchall())
conn.close()
