"""Inventory Management System."""


products = []


def add_product():
    """Add a new product to inventory."""
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Product added successfully.")


def display_products():
    """Display all products."""
    if len(products) == 0:
        print("No products available.")
        return

    print("\n--- PRODUCTS ---")

    for product in products:
        print(
            product["name"],
            "| Price:", product["price"],
            "| Quantity:", product["quantity"]
        )


def search_product():
    """Search for a product by name."""
    name = input("Enter product name to search: ")

    for product in products:
        if product["name"].lower() == name.lower():
            print("Product found:", product)
            return

    print("Product not found.")


def update_quantity():
    """Update the quantity of an existing product."""
    name = input("Enter product name: ")

    for product in products:
        if product["name"].lower() == name.lower():
            quantity = int(input("Enter new quantity: "))
            product["quantity"] = quantity
            print("Quantity updated.")
            return

    print("Product not found.")


def calculate_inventory_value():
    """Calculate the total value of all inventory."""
    total = 0

    for product in products:
        total = total + product["price"] * product["quantity"]

    print("Total inventory value:", total)


add_product()
add_product()
display_products()
search_product()
update_quantity()
calculate_inventory_value()