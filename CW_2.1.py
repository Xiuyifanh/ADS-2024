import time
from random import randint as randomizer_func
from inputs import inputs as input_list


def primality_check(n, iteration=5):
    if n in (2, 3): return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0: return False # this is base cases
    exp1, remainder = 0, n - 1
    while remainder % 2 == 0:
        exp1 += 1
        remainder //= 2
    for i in range(iteration):
        floor = randomizer_func(2, n - 2)
        main_r = pow(floor, remainder, n)
        if main_r == 1 or main_r == n - 1 or any(pow(floor, 2 ** j * remainder, n) == n - 1 for j in range(exp1)):
            continue
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
             and primality_check(num)
             for num in [palindrome])):
            special_found_list.append(palindrome)
        palindrome = next(pali_check)

    return special_found_list


def process_and_print_input_ranges(m, n):
    start_time = time.time()
    special_pull = appender(m, n)
    print(f"Input (m, n): {(m, n)}")
    print(f"Total Palindromic Prime Numbers Found: {len(special_pull)}")
    print(f"Execution Time: {time.time() - start_time:.5f} seconds")
    if len(special_pull) <= 6:
        print(f"List of Palindromic Prime Numbers: {', '.join(map(str, special_pull))}")
    else:
        print(
            f"First and Last 3 Palindromic Prime Numbers: {', '.join(map(str, special_pull[:3] + special_pull[-3:]))}")
    print('---')


for begin, terminate in input_list:
    process_and_print_input_ranges(begin, terminate)
