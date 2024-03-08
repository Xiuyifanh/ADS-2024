import time

class SpecialNumbers:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def sieve_of_eratosthenes(limit):
        primes = []
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for p in range(2, int(limit**0.5) + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, limit + 1, p):
                    sieve[i] = False
        for p in range(int(limit**0.5) + 1, limit + 1):
            if sieve[p]:
                primes.append(p)
        return primes

    @staticmethod
    def palindrome_number_generator(start, end):
        yield 0
        lower = 1
        while True:
            higher = lower * 10
            for i in range(lower, higher):
                s = str(i)
                palindrome = int(s + s[-2::-1])
                if palindrome >= start and palindrome < end:
                    yield palindrome
            for i in range(lower, higher):
                s = str(i)
                palindrome = int(s + s[::-1])
                if palindrome >= start and palindrome < end:
                    yield palindrome
            lower = higher

    @staticmethod
    def palindromic_primes_in_range(start, end):
        primes = SpecialNumbers.sieve_of_eratosthenes(int(end**0.5))
        prime_palindromes = []
        for palindrome in SpecialNumbers.palindrome_number_generator(start, end):
            if all(palindrome % p != 0 for p in primes):
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

        for idx, (x, y) in enumerate(test_cases, 1):
            print(f"Test case {idx}:")
            start_time = time.time()
            prime_palindromes = SpecialNumbers.palindromic_primes_in_range(x, y)
            elapsed_time = time.time() - start_time
            first_three = prime_palindromes[:3]
            last_three = prime_palindromes[-3:]
            print(f"{len(prime_palindromes)}: {first_three} ... {last_three}")
            print(f"Test case {idx} completed in {elapsed_time:.3f} seconds.\n")

# Run test cases
SpecialNumbers.run_test_cases()
