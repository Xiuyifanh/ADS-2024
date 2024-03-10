import time
from sympy import isprime as primality_check


def pali_maker(length):
    palindromes = []
    start = 10 ** ((length - 1) // 2)
    end = 10 ** ((length + 1) // 2)
    for num in range(start, end):  # you're using the range to know where to start and stop
        s = str(
            num)  # first step you convert / cast the number to a string [str] for easier manipulation in the next step
        palindrome = int(s + s[-(
                    length % 2) - 1::-1])  # after you should cast back to integer with maybe inner lambda function? for main calc
        palindromes.append(palindrome)  # lastly append palis that were created to the empty declared list [palindromes]
    return palindromes


def finder(m, n):
    special_numbers = []
    max_length = len(str(n))
    for length in range(len(str(m)), max_length + 1):  # maybe this?
        palindromes = pali_maker(length)
        for palindrome in palindromes:
            if m <= palindrome <= n and primality_check(palindrome):  # basic AND operator check for primality and range
                special_numbers.append(palindrome)
    return special_numbers  # ---> Nihaar encountered some problem? [debug]


def process_and_print_input_ranges():  # MAJOR change to input accepted, no harcoded values instead user_input
    while True:
        m = input("Enter a positive value for m: ")
        n = input("Enter a positive value for n: ")

        try:
            m = abs(int(float(m)))
            n = abs(int(float(n)))

            if 0 < m < n:
                print("-----------------------------------------------------------------------------------")
                break
            else:
                print("-----------------------------------------------------------------------------------")
                print("Please enter positive numbers for m and n.")
        except ValueError:
            print("-----------------------------------------------------------------------------------")
            print("Please enter valid positive numbers for m and n.")

    start_time = time.time()
    special_numbers = finder(m, n)
    print(f"Input (m, n): {(m, n)}")
    print(f"Total Special Numbers: {len(special_numbers)}")
    print(f"Execution Time: {time.time() - start_time:.5f} seconds")
    if len(special_numbers) <= 6:
        print(f"List of special numbers: {', '.join(map(str, special_numbers))}")
    else:
        print(
            f"First and last 3 special numbers: {', '.join(map(str, special_numbers[:3] + special_numbers[-3:]))}")
    print('---')


process_and_print_input_ranges()
