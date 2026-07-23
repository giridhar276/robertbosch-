from src.product_repository import insert_product, fetch_all_products, find_products, change_quantity, remove_product, fetch_inventory_summary

def add_product(name, category, price, quantity):
    if not name or not category:
        raise ValueError('Name and category are required.')
    if price < 0 or quantity < 0:
        raise ValueError('Price and quantity cannot be negative.')
    return insert_product(name, category, price, quantity)

def list_products():
    return fetch_all_products()

def search_products(keyword):
    return find_products(keyword)

def update_quantity(product_id, quantity):
    if quantity < 0:
        raise ValueError('Quantity cannot be negative.')
    return change_quantity(product_id, quantity) > 0

def delete_product(product_id):
    return remove_product(product_id) > 0

def inventory_summary():
    total_products, total_units, inventory_value = fetch_inventory_summary()
    return {'total_products': total_products, 'total_units': total_units, 'inventory_value': inventory_value}
