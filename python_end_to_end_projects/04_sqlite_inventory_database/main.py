from src.database import initialize_database
from src.product_service import add_product, list_products, search_products, update_quantity, delete_product, inventory_summary

def menu():
    print("\n=== Inventory Management System ===")
    print("1. Add product")
    print("2. View all products")
    print("3. Search products")
    print("4. Update product quantity")
    print("5. Delete product")
    print("6. Inventory summary")
    print("0. Exit")

def main():
    initialize_database()
    while True:
        menu()
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                add_product(input("Name: ").strip(), input("Category: ").strip(), float(input("Price: ")), int(input("Quantity: ")))
                print("Product added.")
            elif choice == "2":
                print("\nID | Name | Category | Price | Quantity")
                print("-" * 60)
                for r in list_products():
                    print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]:.2f} | {r[4]}")
            elif choice == "3":
                for r in search_products(input("Keyword: ").strip()):
                    print(r)
            elif choice == "4":
                ok = update_quantity(int(input("Product ID: ")), int(input("New quantity: ")))
                print("Updated." if ok else "Product not found.")
            elif choice == "5":
                ok = delete_product(int(input("Product ID: ")))
                print("Deleted." if ok else "Product not found.")
            elif choice == "6":
                s = inventory_summary()
                print(f"Total products: {s['total_products']}")
                print(f"Total units: {s['total_units']}")
                print(f"Inventory value: {s['inventory_value']:.2f}")
            elif choice == "0":
                print("Application closed.")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a valid numeric value.")
        except Exception as e:
            print(f"Operation failed: {e}")

if __name__ == '__main__':
    main()
