"""Menu-driven Banking Application."""


balance = 10000
transactions = []


def check_balance():
    """Display the current account balance."""
    print("Current balance:", balance)


def deposit():
    """Deposit money into the account."""
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        transactions.append(f"Deposited: {amount}")
        print("Deposit successful.")
    else:
        print("Invalid amount.")


def withdraw():
    """Withdraw money if sufficient balance is available."""
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance = balance - amount
        transactions.append(f"Withdrawn: {amount}")
        print("Withdrawal successful.")


def show_history():
    """Display all banking transactions."""
    print("\n--- TRANSACTION HISTORY ---")

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)


# Initialization: start the banking menu
while True:

    # Condition: continue until the user chooses Exit
    print("\n--- BANKING MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        show_history()

    elif choice == "5":
        print("Thank you for using the banking application.")

        # Termination: exit when user selects option 5
        break

    else:
        print("Invalid choice.")
