import math
import time
class SpecialNumbers:
    @staticmethod
    def prime_siever(limit):  # prime number generation using the segmented sieve of Eratosthenes
        primes = []  # create an empty list to store prime numbers
        sieve = [True] * (
                    limit + 1)  # Create a boolean list to label numbers as prime or composite
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime, so mark them as False
        for p in range(2, int(math.sqrt(limit)) + 1):  # Loop through numbers from 2 to the square root of the limit
            if sieve[p]:  # If the current number is labelled as prime
                primes.append(p)  # Add it to the list of primes
                for i in range(p * p, limit + 1, p):  # label all multiples of the current prime as composite.
                    sieve[i] = False
        # Add remaining primes greater than the square root of the limit.
        for p in range(max(2, int(math.sqrt(limit)) + 1), limit + 1):
            if sieve[p]:  # If the current number is marked as prime:
                primes.append(p)  # Add it to the list of primes.
        return primes  # Return the list of prime numbers.

    @staticmethod
    def palindrome_machine(start, end):  # This function generates palindromic numbers within a specified range
        palindromes = []  # create and initialise an empty list to store palindromes
        for length in range(len(str(start)), len(str(end)) + 1):  # Loop through palindromes from length of start to end
            if length == 1:  # For single-digit palindromes, include primes 2, 3, 5, and 7.
                for num in range(max(2, start), min(10, end) + 1):
                    if num in {2, 3, 5, 7}:  # If the number is a single-digit prime:
                        palindromes.append(num)  # Add it to the list of palindromes
            elif length % 2 == 0:  # For even-length, generate numbers and their mirror images;
                for num in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
                    palindrome = int(str(num) + str(num)[::-1])  # and check if they are palindromes.
                    if start <= palindrome <= end and palindrome > 10:
                        palindromes.append(palindrome)  # add it to the palindrome list
            else:  # else cmd for odd-length palindromes;
                for num in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
                    for middle in range(10):
                        palindrome = int(str(num) + str(middle) + str(num)[::-1])  # include a middle digit
                        if start <= palindrome <= end and palindrome > 10:  # generate palindromes w/ their mirror img
                            palindromes.append(palindrome)

        return palindromes  # returns the palindromes

    @staticmethod
    def merger(start, end):
        # This function merges the lists of prime numbers and palindromes to find prime palindromes.
        limit = int(math.sqrt(end)) + 1  # Calculate the limit for generating primes.
        primes = SpecialNumbers.prime_siever(limit)  # Generate prime numbers up to the square root of end.
        palindromes = SpecialNumbers.palindrome_machine(start, end)  # Generate palindromes within the specified range.
        prime_palindromes = []  # Initialize an empty list to store prime palindromes.

        # Loop through each palindrome.
        for palindrome in palindromes:
            is_prime = True  # Assume the palindrome is prime initially.
            # If the palindrome is in the list of single-digit primes, add it to the list of prime palindromes.
            if palindrome in {2, 3, 5, 7, 11}:
                prime_palindromes.append(palindrome)
                continue
            # Loop through each prime number.
            for prime in primes:
                # If the square of the prime number is greater than the palindrome, break the loop.
                if prime * prime > palindrome:
                    break
                # If the palindrome is divisible by any prime number, it is not prime.
                if palindrome % prime == 0:
                    is_prime = False
                    break
            # If the palindrome is prime, add it to the list of prime palindromes.
            if is_prime:
                prime_palindromes.append(palindrome)
        return prime_palindromes  # Return the list of prime palindromes.

    @staticmethod
    def run_test_cases():  # Define test cases as tuples of (start, end) ranges.
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
        for idx, (start, end) in enumerate(test_cases, 1):  # Loop through each test case.
            print(f"Test case {idx}:")  # proper indexing for each testcase
            start_time = time.time()  # Record the start time.
            prime_palindromes = SpecialNumbers.merger(start, end)  # Find prime palindromes within the range.
            elapsed_time = time.time() - start_time  # Calculate the elapsed time.
            if len(prime_palindromes) >= 6:  # print the result out for each test case.
                first_three = prime_palindromes[:3]
                last_three = prime_palindromes[-3:]
                print(f"{len(prime_palindromes)}: {first_three} ... {last_three}")
            else:  # if less than six
                print(f"{len(prime_palindromes)}: {prime_palindromes}")
            print(f"Test case {idx} completed in {elapsed_time:.3f} seconds.\n")


SpecialNumbers.run_test_cases()  # Run the test cases.
