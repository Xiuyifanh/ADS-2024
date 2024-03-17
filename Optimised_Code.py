import time
import random


def prime_checker(num, k=3):
    beginning_primes = [2, 3, 5, 7]  # List of beginning primes
    if num in beginning_primes:  # If the number is in the beginning primes list, it's considered prime
        return True
    if num <= 1 or any(num % p == 0 for p in beginning_primes):  # If the number is less than or equal to 1
        # or divisible by any beginning prime, it's not prime, return false
        return False
    r, d = 0, num - 1
    while d % 2 == 0:  # Get the values of r and d according to the formula (num - 1) = (2^r) * d
        r += 1
        d //= 2
        for _ in range(k):  # Repeat Miller-Rabin primality test k times as initialised before
            a = random.randint(2, num - 1)  # Choose a random integer a such that 2 <= a <= num - 1
            x = pow(a, d, num)  # Compute x = a^d mod num
            if x == 1 or x == num - 1:  # If x == 1 or x == num - 1, continue with the next iteration
                continue
            for _ in range(r - 1):  # Repeat the squaring and modulo operation r - 1 times
                x = pow(x, 2, num)
                if x == num - 1:  # If x == num - 1, break out of the loop
                    break
            else:  # any other case;
                return False  # If x is neither 1 nor num - 1, return False (not prime)
    return True  # finally, if the number passes all tests, return True (prime)


class SpecialNumbers:
    @staticmethod
    def palindrome_machine(start, end):  # This function generates palindromic numbers within a specified range
        palindromes = []  # create and initialise an empty list to store palindromes
        for length in range(len(str(start)), len(str(end)) + 1):  # Loop through palindromes from length of start to end
            if length == 1:  # For single-digit palindromes, include primes 2, 3, 5, and 7
                for num in range(max(2, start), min(10, end) + 1):
                    if num in {2, 3, 5, 7}:  # If the number is a single-digit prime:
                        palindromes.append(num)  # Add it to the list of palindromes
            elif length % 2 == 0:  # For even-length, generate numbers and their mirror images;
                for num in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
                    palindrome = int(str(num) + str(num)[::-1])  # and check if they are palindromes
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
    def merger(start, end):  # merger function for the lists of prime numbers and palindromes to find prime palindromes
        palindromes = SpecialNumbers.palindrome_machine(start, end)  # generate palindromes within the specified range
        prime_palindromes = []  # create an empty list to store special numbers.
        for palindrome in palindromes:  # Loop through each palindrome.
            # If the palindrome is in the list of single-digit primes, add it to the list of special numbers.
            if palindrome in {2, 3, 5, 7, 11}:
                prime_palindromes.append(palindrome)
                continue
            if prime_checker(palindrome):   # If the palindrome matches any generated prime number, it is a special
                prime_palindromes.append(palindrome)   # append the list
        return prime_palindromes  # return all palindromes

    @staticmethod
    def run_test_cases():   # Define test cases as tuples of (start, end) ranges.
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
            else:  # if less than six special numbers
                print(f"{len(prime_palindromes)}: {prime_palindromes}")
            print(f"Test case {idx} completed in {elapsed_time:.3f} seconds.\n")

SpecialNumbers.run_test_cases()  # Run the test cases.

