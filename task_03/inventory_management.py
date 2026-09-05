
"""Inventory Management System."""


products = []


def get_positive_price():
    """Get a valid positive price from the user."""
    while True:
        try:
            price = float(input("Enter price: "))

            if price <= 0:
                print("Price must be greater than 0.")
                continue

            return price

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_positive_quantity():
    """Get a valid positive quantity from the user."""
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            return quantity

        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def add_product():
    """Add a new product to inventory."""
    name = input("Enter product name: ")

    price = get_positive_price()
    quantity = get_positive_quantity()

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
            quantity = get_positive_quantity()
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


# Initialization: start the inventory menu
while True:

    # Condition: continue until the user chooses Exit
    print("\n--- INVENTORY MANAGEMENT ---")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Calculate Total Inventory Value")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        display_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_quantity()

    elif choice == "5":
        calculate_inventory_value()

    elif choice == "6":
        print("Inventory management closed.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
