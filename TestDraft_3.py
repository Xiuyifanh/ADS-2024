import time
from sympy import isprime

class SpecialNumbers:
    @staticmethod
    def palindrome_number_generator():
        yield 0
        lower = 1
        while True:
            higher = lower * 10
            for i in range(lower, higher):
                s = str(i)
                yield int(s + s[-2::-1])
            for i in range(lower, higher):
                s = str(i)
                yield int(s + s[::-1])
            lower = higher

    @staticmethod
    def palindromes(lower, upper):
        all_palindrome_numbers = SpecialNumbers.palindrome_number_generator()
        palindrome_list = []
        for p in all_palindrome_numbers:
            if p >= upper:
                break
            if p >= lower:
                palindrome_list.append(p)
        return palindrome_list

    @staticmethod
    def prime(n):
        return isprime(n)

    @staticmethod
    def count_palindromic_primes(start, end):
        special_numbers = []
        for p in SpecialNumbers.palindromes(start, end):
            if SpecialNumbers.prime(p):
                special_numbers.append(p)
        return special_numbers

    @staticmethod
    def run_test_cases():
        test_cases = [
            (1, 2000),
            (100, 10000),
            (20000, 80000),
            (100000, 2000000),
            (2000000, 9000000),
            (10000000, 100000000),
            (100000000, 400000000),
            (1100000000, 15000000000),
            (15000000000, 100000000000),
            (1, 1000000000000)
        ]

        for idx, (x, y) in enumerate(test_cases, 1):
            print(f"Test case {idx}:")
            start_time = time.time()
            special_numbers = SpecialNumbers.count_palindromic_primes(x, y)
            elapsed_time = time.time() - start_time
            first_three = special_numbers[:3]
            last_three = special_numbers[-3:]
            print(f"{len(special_numbers)}: {first_three} ... {last_three}")
            print(f"Test case {idx} completed in {elapsed_time:.9f} seconds.\n")

# Run test cases
SpecialNumbers.run_test_cases()
