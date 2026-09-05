"""Employee Salary Analyzer."""


def calculate_total_salary(salaries):
    """Calculate total payroll."""
    total = 0

    for salary in salaries:
        total = total + salary

    return total


def calculate_average_salary(salaries):
    """Calculate average salary."""
    total = calculate_total_salary(salaries)
    return total / len(salaries)


def find_highest_salary(salaries):
    """Find the highest salary without using max()."""
    highest = salaries[0]

    for salary in salaries:
        if salary > highest:
            highest = salary

    return highest


def find_lowest_salary(salaries):
    """Find the lowest salary without using min()."""
    lowest = salaries[0]

    for salary in salaries:
        if salary < lowest:
            lowest = salary

    return lowest


def employees_above_average(salaries, average):
    """Return salaries that are above average."""
    result = []

    for salary in salaries:
        if salary > average:
            result.append(salary)

    return result


salaries = [25000, 32000, 45000, 28000, 60000]

total = calculate_total_salary(salaries)
average = calculate_average_salary(salaries)
highest = find_highest_salary(salaries)
lowest = find_lowest_salary(salaries)
above_average = employees_above_average(salaries, average)

print("Total payroll:", total)
print("Average salary:", average)
print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Employees above average:", above_average)