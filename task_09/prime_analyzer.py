"""Prime Number Analyzer."""


def is_prime(number):
    """Return True if a number is prime."""
    if number < 2:
        return False

    i = 2

    # Condition: check divisors until i reaches number
    while i < number:

        if number % i == 0:
            return False

        # Update: move to the next possible divisor
        i = i + 1

    return True


def find_primes(start, end):
    """Return all prime numbers in the given range."""
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


def analyze_primes(primes):
    """Display prime count, sum and largest prime."""

    if len(primes) == 0:
        print("No prime numbers found.")
        return

    total = 0

    for prime in primes:
        total = total + prime

    largest = primes[0]

    for prime in primes:
        if prime > largest:
            largest = prime

    print("Prime numbers:", primes)
    print("Number of primes:", len(primes))
    print("Sum of primes:", total)
    print("Largest prime:", largest)


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

primes = find_primes(start, end)

analyze_primes(primes)