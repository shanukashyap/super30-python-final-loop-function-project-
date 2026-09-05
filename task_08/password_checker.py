"""Password Strength Checker."""


def check_password(password):
    """Check password requirements and return a strength result."""

    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    for character in password:

        if character.isupper():
            has_upper = True

        elif character.islower():
            has_lower = True

        elif character.isdigit():
            has_number = True

        else:
            has_special = True

    if (
        len(password) >= 8
        and has_upper
        and has_lower
        and has_number
        and has_special
    ):
        return "Strong password"

    return "Weak password"


password = input("Enter password: ")

result = check_password(password)

print(result)