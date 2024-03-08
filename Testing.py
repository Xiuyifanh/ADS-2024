from sympy import isprime
import time

class SpecialNumbers:
    @staticmethod
    def generate_palindromes(start, end):
        palindromes = []
        for length in range(len(str(start)), len(str(end)) + 1):
            if length == 1:
                for num in range(start, min(10, end) + 1):
                    if num not in {2, 4, 5, 6, 8} and num % 11 != 0 and num % 7 != 0 and num % 9 != 0:
                        palindromes.append(num)
            elif length % 2 == 0:
                for num in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
                    palindrome = int(str(num) + str(num)[::-1])
                    if start <= palindrome <= end and palindrome > 10:
                        if palindrome % 11 != 0 and palindrome % 7 != 0 and palindrome % 9 != 0:
                            palindromes.append(palindrome)
            else:
                for num in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
                    for middle in range(10):
                        palindrome = int(str(num) + str(middle) + str(num)[::-1])
                        if start <= palindrome <= end and palindrome > 10:
                            if palindrome % 11 != 0 and palindrome % 7 != 0 and palindrome % 9 != 0:
                                palindromes.append(palindrome)
        return palindromes

    @staticmethod
    def count_palindromic_primes(start, end):
        special_numbers = []
        for num in SpecialNumbers.generate_palindromes(start, end):
            if isprime(num):
                special_numbers.append(num)
        num_special_numbers = len(special_numbers)
        first_three = special_numbers[:3]
        last_three = special_numbers[-3:]
        return num_special_numbers, first_three, last_three

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
            num_special_numbers, first_three, last_three = SpecialNumbers.count_palindromic_primes(x, y)
            elapsed_time = time.time() - start_time
            print(f"{num_special_numbers}: {first_three} ... {last_three}")
            print(f"Test case {idx} completed in {elapsed_time:.9f} seconds.\n")

# Run test cases
SpecialNumbers.run_test_cases()
