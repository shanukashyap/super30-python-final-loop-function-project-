"""Student Result Management System."""


def accept_marks():
    """Accept marks for five subjects and return them as a list."""
    marks = []

    for i in range(1, 6):

        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return marks


def calculate_total(marks):
    """Calculate and return the total marks."""
    total = 0

    for mark in marks:
        total = total + mark

    return total


def calculate_percentage(total, number_of_subjects):
    """Calculate and return the percentage."""
    return total / number_of_subjects


def assign_grade(percentage):
    """Assign a grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(marks):
    """Return Pass if all subjects have at least 40 marks."""
    for mark in marks:
        if mark < 40:
            return "Fail"

    return "Pass"


def display_result(marks, total, percentage, grade, result):
    """Display the complete student result."""
    print("\n--- STUDENT RESULT ---")
    print("Marks:", marks)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("Result:", result)


marks = accept_marks()
total = calculate_total(marks)
percentage = calculate_percentage(total, len(marks))
grade = assign_grade(percentage)
result = check_pass_fail(marks)

display_result(marks, total, percentage, grade, result)
