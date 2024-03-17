import time
import random
def prime_checker(num, k=3):
    beginning_primes = [2, 3, 5, 7]
    if num in beginning_primes:  
        return True
    if num <= 1 or any(num % p == 0 for p in beginning_primes):
        return False
    r, d = 0, num - 1  
    while d % 2 == 0:  
        r += 1  
        d //= 2
        for _ in range(k):  
            a = random.randint(2, num - 1)  
            x = pow(a, d, num)  
            if x == 1 or x == num - 1:  
                continue
            for _ in range(r - 1):  
                x = pow(x, 2, num)  
                if x == num - 1:  
                    break
            else:  
                return False
    return True  

class SpecialNumbers:
    @staticmethod
    def palindrome_machine(start, end):
        palindromes = []
        for length in range(len(str(start)), len(str(end)) + 1):
            if length == 1:
                for num in range(max(2, start), min(10, end) + 1):  
                    if num in {2, 3, 5, 7}:  
                        palindromes.append(num)
            elif length % 2 == 0:
                for num in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
                    palindrome = int(str(num) + str(num)[::-1])
                    if start <= palindrome <= end and palindrome > 10:
                        palindromes.append(palindrome)
            else:
                for num in range(10 ** (length // 2 - 1), 10 ** (length // 2)):
                    for middle in range(10):
                        palindrome = int(str(num) + str(middle) + str(num)[::-1])
                        if start <= palindrome <= end and palindrome > 10:
                            palindromes.append(palindrome)
        return palindromes

    @staticmethod
    def merger(start, end):
        palindromes = SpecialNumbers.palindrome_machine(start, end)
        prime_palindromes = []
        for palindrome in palindromes:
            if palindrome in {2, 3, 5, 7, 11}: 
                prime_palindromes.append(palindrome)
                continue
            if prime_checker(palindrome):
                prime_palindromes.append(palindrome)
        return prime_palindromes

    @staticmethod
    def run_test_cases():
        test_cases = [
            (1, 1000),
            (1, 10000),
            (1, 100000),
            (1, 1000000),
            (1, 10000000),
            (1, 100000000),
            (1, 1000000000),
            (1, 10000000000),
            (1, 100000000000),
            (1, 1000000000000),
            (1, 10000000000000),
            (1, 100000000000000)
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
