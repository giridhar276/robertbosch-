import sqlite3
from pathlib import Path

DATABASE_PATH = Path('data/inventory.db')

def get_connection():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)

def initialize_database():
    with get_connection() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL CHECK(price >= 0),
                quantity INTEGER NOT NULL CHECK(quantity >= 0)
            )
        """)
        if con.execute('SELECT COUNT(*) FROM products').fetchone()[0] == 0:
            con.executemany(
                'INSERT INTO products(name, category, price, quantity) VALUES (?, ?, ?, ?)',
                [('Laptop','Electronics',65000,10),('Keyboard','Accessories',1500,25),('Office Chair','Furniture',8500,8),('Notebook','Stationery',120,50)]
            )
