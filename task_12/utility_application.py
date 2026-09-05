"""Super30 Python Utility Application."""


def calculator():
    """Perform basic arithmetic operations."""

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid operator.")


def palindrome_checker():
    """Check whether a string is a palindrome."""

    text = input("Enter text: ")

    if text == text[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


def prime_checker():
    """Check whether a number is prime."""

    number = int(input("Enter number: "))

    if number < 2:
        print("Not a prime number.")
        return

    is_prime = True
    i = 2

    while i < number:

        if number % i == 0:
            is_prime = False
            break

        i = i + 1

    if is_prime:
        print("Prime number.")
    else:
        print("Not a prime number.")


def factorial():
    """Calculate factorial using a while loop."""

    number = int(input("Enter number: "))

    result = 1
    i = 1

    while i <= number:
        result = result * i
        i = i + 1

    print("Factorial:", result)


def multiplication_table():
    """Display multiplication table."""

    number = int(input("Enter number: "))

    i = 1

    while i <= 10:
        print(number, "x", i, "=", number * i)
        i = i + 1


def number_analyzer():
    """Analyze a number as positive, negative, even or odd."""

    number = int(input("Enter number: "))

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


# Initialization: start the utility application menu
while True:

    # Condition: continue until the user selects Exit
    print("\n===== SUPER30 PYTHON UTILITY =====")
    print("1. Calculator")
    print("2. Palindrome Checker")
    print("3. Prime Checker")
    print("4. Factorial")
    print("5. Multiplication Table")
    print("6. Number Analyzer")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        palindrome_checker()

    elif choice == "3":
        prime_checker()

    elif choice == "4":
        factorial()

    elif choice == "5":
        multiplication_table()

    elif choice == "6":
        number_analyzer()

    elif choice == "7":
        print("Thank you for using Super30 Python Utility.")

        # Termination: stop when the user selects Exit
        break

    else:
        print("Invalid choice. Please try again.")