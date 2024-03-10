import time


def pali_maker(n, lower_bound, upper_bound):
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


def eratosthenes_sieveV2(n):
    primes = []
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes


def finder(lower_bound, upper_bound):
    primes = eratosthenes_sieveV2(upper_bound)
    special_numbers = []
    for prime in primes:
        if lower_bound <= prime <= upper_bound and pali_maker(prime, lower_bound, upper_bound):
            special_numbers.append(prime)
    return special_numbers


def process_input_range(input_range):
    m, n = input_range
    start_time = time.time()
    special_numbers = finder(m, n)
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
