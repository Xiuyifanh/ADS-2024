import time
import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    max_divisor = math.isqrt(n) + 1
    for i in range(5, max_divisor, 6):  # here I'm applying a form of trial division as primes over 3 in form 6k +- 1
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True



def pali_maker():
    yield 0
    for i in range(1, 10):
        yield i
    for constant in range(2, 20):
        for half in range(10 ** (constant // 2 - 1), 10 ** (constant // 2)):
            half_str = str(half)
            if constant % 2 == 0:
                yield int(half_str + half_str[::-1])
            else:
                for mid in range(10):
                    yield int(half_str + str(mid) + half_str[::-1])


def appender(start, end):
    special_found_list = []
    pali_check = pali_maker()
    palindrome = next(pali_check)

    while palindrome <= end:
        if (all
            (start <= num <= end
             and is_prime(num)
             for num in [palindrome])):
            special_found_list.append(palindrome)
        palindrome = next(pali_check)

    return special_found_list


def process_and_print_input_ranges():
    while True:
        m = input("Enter a positive value for m: ")
        n = input("Enter a positive value for n: ")

        try:
            m = abs(int(float(m)))
            n = abs(int(float(n)))

            if m < n:
                print("-----------------------------------------------------------------------------------")
                break
            else:
                print("-----------------------------------------------------------------------------------")
                print("Please enter m less than n.")
        except ValueError:
            print("-----------------------------------------------------------------------------------")
            print("Please enter valid positive numbers for m and n.")

    start_time = time.time()
    special_pull = appender(m, n)
    print(f"Input (m, n): {(m, n)}")
    print(f"Total Palindromic Prime Numbers: {len(special_pull)}")
    print(f"Execution Time: {time.time() - start_time:.5f} seconds")
    if len(special_pull) <= 6:
        print(f"List of Palindromic Prime Numbers: {', '.join(map(str, special_pull))}")
    else:
        print(
            f"First and Last 3 Palindromic Prime Numbers: {', '.join(map(str, special_pull[:3] + special_pull[-3:]))}")
    print('---')


process_and_print_input_ranges()
