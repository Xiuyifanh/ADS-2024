import time  # Importing the time module for time-related functions
from math import isqrt  # Importing the isqrt function from the math module for integer square root

# Function to generate palindromic numbers within a specified range
def generate_palindromic_numbers(start, end):
    # Nested function to generate palindromic numbers of specified digits
    def generate_palindromes(digits):
        # Check if the number of digits is 1
        if digits == 1:
            # Generate palindromes from 1 to 9 for single-digit numbers
            for i in range(1, 10):
                yield i  # Yield the palindrome
        # Check if the number of digits is even
        elif digits % 2 == 0:
            # Calculate half of the digits
            half = digits // 2
            # Generate palindromes with even length
            half_range = range(10 ** (half - 1), 10 ** half)
            for i in half_range:
                # Construct the palindrome by mirroring the left half
                palindrome = int(str(i) + str(i)[::-1])
                # Check if the palindrome is within the specified range
                if start <= palindrome <= end:
                    yield palindrome  # Yield the palindrome
        else:
            # Calculate half of the digits for odd-length palindromes
            half = digits // 2
            # Generate palindromes with odd length
            half_range = range(10 ** (half - 1), 10 ** half)
            for i in half_range:
                for j in range(10):
                    # Construct the palindrome by inserting a digit in the middle
                    palindrome = int(str(i) + str(j) + str(i)[::-1])
                    # Check if the palindrome is within the specified range
                    if start <= palindrome <= end:
                        yield palindrome  # Yield the palindrome

    start_digits = len(str(start))  # Calculate the number of digits in the start number
    end_digits = len(str(end))  # Calculate the number of digits in the end number

    start_time = time.time()  # Record the start time
    # Generate palindromic numbers for each number of digits in the specified range
    for digits in range(start_digits, end_digits + 1):
        yield from generate_palindromes(digits)  # Yield palindromes

    end_time = time.time()  # Record the end time
    print("Time taken:", end_time - start_time, "seconds")  # Print the time taken

# Function to check if a number is prime
def is_prime(palindrome):
    if palindrome < 2:  # Check if the number is less than 2
        return False  # Return False for numbers less than 2
    if palindrome == 2:  # Check if the number is 2
        return True  # Return True for 2, which is prime
    if palindrome % 2 == 0:  # Check if the number is even
        return False  # Return False for even numbers other than 2
    # Iterate through odd numbers up to the square root of the number
    for i in range(3, isqrt(palindrome) + 1, 2):
        # Check if the number is divisible by any odd number
        if palindrome % i == 0:
            return False  # Return False if divisible
    return True  # Return True if not divisible by any odd number

# Function to identify and print special numbers (prime palindromic numbers)
def special_numbers(num1, num2):
    special_num = []  # Initialize an empty list to store special numbers
    # Iterate through palindromic numbers within the specified range
    for palindrome in generate_palindromic_numbers(num1, num2):
        # Check if the palindrome is prime
        if is_prime(palindrome):
            special_num.append(palindrome)  # Append prime palindrome to the list
    # Check the number of special numbers found
    if len(special_num) < 6:
        print(special_num)  # Print the list of special numbers if fewer than six
    else:
        end = len(special_num)  # Get the total number of special numbers
        # Print the total length and first three and last three special numbers
        print(f"Length: {len(special_num)}"
              f"\n{special_num[0]}, {special_num[1]}, {special_num[2]}, {special_num[end - 3]}, "
              f"{special_num[end - 2]}, {special_num[end - 1]}")


num1 = int(input("Enter the start of the range: "))  # Lets user enter the start of the range
num2 = int(input("Enter the end of the range: "))  # Lets user enter the end of the range
special_numbers(num1, num2)  # Runs the code based on the values entered for num1 and num2
