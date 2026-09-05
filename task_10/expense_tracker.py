
"""Expense Tracker Application."""


expenses = []


def get_positive_amount():
    """Get a valid positive expense amount."""
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_expense():
    """Add an expense to the tracker."""
    name = input("Enter expense name: ")

    amount = get_positive_amount()

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added.")


def view_expenses():
    """Display all recorded expenses."""
    if len(expenses) == 0:
        print("No expenses found.")
        return

    for expense in expenses:
        print(expense["name"], ":", expense["amount"])


def calculate_total():
    """Calculate total expenses."""
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total expenses:", total)


def highest_expense():
    """Find the highest expense."""
    if len(expenses) == 0:
        print("No expenses available.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("Highest expense:", highest["name"], highest["amount"])


# Initialization: start the expense tracker menu
while True:

    # Condition: continue until the user chooses Exit
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Highest Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        highest_expense()

    elif choice == "5":
        print("Expense tracker closed.")

        # Termination: stop when Exit is selected
        break

    else:
        print("Invalid choice.")
