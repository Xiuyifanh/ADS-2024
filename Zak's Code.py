# Checks if a number is prime
def prime(number):
    # If a number is less than 2, it is not prime
    if number < 2:
        return False
    # 2 is the only even prime
    elif number == 2:
        return True
    # If a number is even, it is not prime, unless it is 2
    elif number % 2 == 0:
        return False
    else:
        # Calculates if the number is divisible by any odd number from 3 to the square root of the number- This is faster way of calculating if a number is prime
        for i in range(3, int(number**0.5)+1, 2):
            if number % i == 0:
                return False
        return True


# Checks if a number is a palindrome
def palindrome(number):
    # Converts number into a string and evaluates if it is the same as the reverse of the string
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


# Function to look for special numbers from a range of numbers
def look_for_special_numbers(lower, higher):
    # Initialises a list which all the special numbers will be appended too
    special_numbers = []
    # For loop to see if any numbers from the range are prime and palindromes by calling the respective functions
    for i in range(lower, higher):
        if prime(i) == True and palindrome(i) == True:
            special_numbers.append(i)

    # count is the amount of special numbers in the given range, which is equal to the length of the list
    count = len(special_numbers)

    # If there are six or less special numbers, print the whole list
    if len(special_numbers) <= 6:
        print(special_numbers)
        print("Amount of Special Numbers: ", count)
    # If there are more than six special numbers, print the first and last three
    else:
        print([special_numbers[0], special_numbers[1], special_numbers[2], special_numbers[len(special_numbers) - 3],
               special_numbers[len(special_numbers) - 2], special_numbers[len(special_numbers) - 1]])
        print("Amount of Special Numbers: ", count)


def run_test_cases():
    # Define test cases as tuples of (start, end) ranges.
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
        look_for_special_numbers(start, end)
        print()


run_test_cases()