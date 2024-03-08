import time


def is_palindrome(n, lower_bound, upper_bound):
    if lower_bound <= n <= upper_bound:
        num = n
        reverse = 0
        while num > 0:
            last_digit = num % 10
            reverse = reverse * 10 + last_digit
            num //= 10
        return n == reverse
    else:
        return False


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_special_numbers_optimized(lower_bound, upper_bound):
    special_numbers = []
    for i in range(max(2, lower_bound), upper_bound + 1):  # Adjusting the range to ensure 2 is included if applicable
        if is_palindrome(i, lower_bound, upper_bound) and is_prime(i):
            special_numbers.append(i)
    return special_numbers


def process_input_range(input_range):
    m, n = input_range
    start_time = time.time()
    special_numbers = find_special_numbers_optimized(m, n)
    end_time = time.time()
    execution_time = end_time - start_time
    return {'Input': (m, n), 'Total': len(special_numbers), 'Special Numbers': special_numbers,
            'Execution Time': execution_time}


inputs = [
    (1, 2000),
    (100, 10000),
    (20000, 80000),
    (100000, 2000000),
    (2_000_000, 9_000_000),
    (10_000_000, 100_000_000),
    (100_000_000, 400_000_000),
    (1_100_000_000, 15_000_000_000),
    (15_000_000_000, 100_000_000_000),
    (1, 1_000_000_000_000)
]
for input_range in inputs:
    result = process_input_range(input_range)
    print(f"Input (m, n): {result['Input']}")
    print(f"Total Special Numbers: {result['Total']}")
    print(f"Execution Time: {result['Execution Time']} seconds")
    if len(result['Special Numbers']) <= 6:
        print(f"List of special numbers: {', '.join(map(str, result['Special Numbers']))}")
    else:
        print(
            f"Showing first and last 3 special numbers: {', '.join(map(str, result['Special Numbers'][:3] + result['Special Numbers'][-3:]))}")
    print('---')
