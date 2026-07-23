from src.database import get_connection

def insert_product(name, category, price, quantity):
    with get_connection() as con:
        cur = con.execute('INSERT INTO products(name, category, price, quantity) VALUES (?, ?, ?, ?)', (name, category, price, quantity))
        return cur.lastrowid

def fetch_all_products():
    with get_connection() as con:
        return con.execute('SELECT product_id, name, category, price, quantity FROM products ORDER BY product_id').fetchall()

def find_products(keyword):
    value = f'%{keyword}%'
    with get_connection() as con:
        return con.execute('SELECT product_id, name, category, price, quantity FROM products WHERE name LIKE ? OR category LIKE ? ORDER BY name', (value, value)).fetchall()

def change_quantity(product_id, quantity):
    with get_connection() as con:
        return con.execute('UPDATE products SET quantity=? WHERE product_id=?', (quantity, product_id)).rowcount

def remove_product(product_id):
    with get_connection() as con:
        return con.execute('DELETE FROM products WHERE product_id=?', (product_id,)).rowcount

def fetch_inventory_summary():
    with get_connection() as con:
        return con.execute('SELECT COUNT(*), COALESCE(SUM(quantity),0), COALESCE(SUM(price*quantity),0) FROM products').fetchone()
