import math
import time

class SpecialNumbers:
    @staticmethod
    def prime_siever(limit):
        primes = []
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for p in range(2, int(math.sqrt(limit)) + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, limit + 1, p):
                    sieve[i] = False
        for p in range(max(2, int(math.sqrt(limit)) + 1), limit + 1):
            if sieve[p]:
                primes.append(p)
        return primes
    @staticmethod
    def palindrome_machine(start, end):
        palindromes = []
        # Generate single-digit palindromes
        for num in range(2, min(10, end) + 1):
            if num in {2, 3, 5, 7}:  # Include single-digit primes
                palindromes.append(num)
        # Generate even-length palindromes
        for num in range(1, int(math.sqrt(end)) + 1):  # Adjust the range based on performance
            palindrome = int(str(num) + str(num)[::-1])
            if palindrome <= end:
                palindromes.append(palindrome)
            else:
                break
        # Generate odd-length palindromes
        for num in range(1, int(math.sqrt(end)) + 1):  # Adjust the range based on performance
            for middle in range(10):
                palindrome = int(str(num) + str(middle) + str(num)[::-1])
                if palindrome <= end:
                    palindromes.append(palindrome)
                else:
                    break
        return [p for p in palindromes if p >= start]
    @staticmethod
    def merger(start, end):
        limit = int(math.sqrt(end)) + 1
        primes = SpecialNumbers.prime_siever(limit)
        palindromes = SpecialNumbers.palindrome_machine(start, end)
        prime_palindromes = []
        for palindrome in palindromes:
            is_prime = True
            for prime in primes:
                if prime * prime > palindrome:
                    break
                if palindrome % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_palindromes.append(palindrome)
        return prime_palindromes
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
        for idx, (start, end) in enumerate(test_cases, 1):
            print(f"Test case {idx}:")
            start_time = time.time()
            prime_palindromes = SpecialNumbers.merger(start, end)
            elapsed_time = time.time() - start_time
            if len(prime_palindromes) >= 6:
                first_three = prime_palindromes[:3]
                last_three = prime_palindromes[-3:]
                print(f"{len(prime_palindromes)}: {first_three} ... {last_three}")
            else:
                print(f"{len(prime_palindromes)}: {prime_palindromes}")
            print(f"Test case {idx} completed in {elapsed_time:.3f} seconds.\n")

SpecialNumbers.run_test_cases()
