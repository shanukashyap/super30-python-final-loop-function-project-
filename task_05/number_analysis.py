"""Number Analysis Tool without min(), max(), or sum()."""


def analyze_numbers(numbers):
    """Return statistical information about a list of numbers."""

    largest = numbers[0]
    smallest = numbers[0]
    total = 0

    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for number in numbers:

        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

        total = total + number

        if number % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1

        if number > 0:
            positive_count = positive_count + 1
        elif number < 0:
            negative_count = negative_count + 1

    average = total / len(numbers)

    return (
        largest,
        smallest,
        total,
        average,
        even_count,
        odd_count,
        positive_count,
        negative_count
    )


numbers = [10, -5, 8, 20, -3, 7, 12]

result = analyze_numbers(numbers)

print("Largest:", result[0])
print("Smallest:", result[1])
print("Total:", result[2])
print("Average:", result[3])
print("Even count:", result[4])
print("Odd count:", result[5])
print("Positive count:", result[6])
print("Negative count:", result[7])