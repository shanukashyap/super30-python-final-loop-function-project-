"""Mini Authentication System."""


correct_username = "admin"
correct_password = "python123"


def login():
    """Allow the user a maximum of three login attempts."""

    attempts = 0
    max_attempts = 3

    # Condition: continue until login succeeds or attempts are exhausted
    while attempts < max_attempts:

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login successful.")
            return True

        attempts = attempts + 1

        print("Login failed.")
        print("Attempts remaining:", max_attempts - attempts)

    print("Maximum login attempts reached.")
    return False


def logout():
    """Display logout message."""
    print("You have been logged out.")


# Main authentication flow
if login():

    # Initialization: user is logged in
    while True:

        print("\n1. Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            logout()

            # Termination: exit after logout
            break

        else:
            print("Invalid choice.")