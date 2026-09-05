
"""Simple Shopping Cart Application."""


cart = []


def get_positive_price():
    """Get a valid positive price from the user."""
    while True:
        try:
            price = float(input("Enter product price: "))

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
    """Add a product to the shopping cart."""
    name = input("Enter product name: ")

    price = get_positive_price()
    quantity = get_positive_quantity()

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(product)
    print("Product added.")


def remove_product():
    """Remove a product from the cart."""
    name = input("Enter product name to remove: ")

    for product in cart:
        if product["name"].lower() == name.lower():
            cart.remove(product)
            print("Product removed.")
            return

    print("Product not found.")


def view_cart():
    """Display all products in the cart."""
    if len(cart) == 0:
        print("Cart is empty.")
        return

    for product in cart:
        print(product)


def calculate_bill():
    """Calculate and display the total bill."""
    total = 0

    for product in cart:
        total = total + product["price"] * product["quantity"]

    print("Total bill:", total)


# Initialization: start the shopping cart menu
while True:

    # Condition: continue until Exit is selected
    print("\n--- SHOPPING CART ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Calculate Bill")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        remove_product()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        calculate_bill()

    elif choice == "5":
        print("Thank you for shopping.")

        # Termination: stop when Exit is selected
        break

    else:
        print("Invalid choice.")
