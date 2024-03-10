import time
from sympy import isprime as primality_check #sympy is efficent but rely on own is_prime!


def pali_maker(length):
    palindromes = []
    start = 10 ** ((length - 1) // 2)
    end = 10 ** ((length + 1) // 2)
    for num in range(start, end): #you're using the range to know where to start and stop
        # first step you convert / cast the number to a string [str] for easier manipulation in the next step
        # Shuhaib note: maybe look at length and construct palindrome accordingly? figure it out
        # after you should cast back to integer with maybe inner lambda function? for main calc
        # the reason you wanted to convert to int is cuz you can calc ::3 and ::-3 and len(list) for total specials
        # lastly append palis that were created to the empty declared list [palindromes]
        pass
    return palindromes




def finder(m, n):
    special_numbers = []
    max_length = len(str(n))
    for length in range(len(str(m)), max_length + 1):
        palindromes = pali_maker(length)
        for palindrome in palindromes:
            if m <= palindrome <= n and primality_check(palindrome):
                special_numbers.append(palindrome)
    return special_numbers


def process_input_range(input_range):
    m, n = input_range
    start_time = time.time()
    special_numbers = finder(m, n)
    end_time = time.time()
    execution_time = end_time - start_time
    return {'Input': (m, n), 'Total': len(special_numbers), 'Special Numbers': special_numbers,
            'Execution Time': execution_time}


inputs = [
    (1, 2000),
    (100, 10000),
    (20000, 80000),
    (100000, 2000000),
    (2_000_000, 9_000_000),
    (10_000_000, 100_000_000),
    (100_000_000, 400_000_000),
    (1_100_000_000, 15_000_000_000),
    (15_000_000_000, 100_000_000_000),
    (1, 1_000_000_000_000)
]
for input_range in inputs:
    result = process_input_range(input_range)
    print(f"Input (m, n): {result['Input']}")
    print(f"Total Special Numbers: {result['Total']}")
    print(f"Execution Time: {result['Execution Time']} seconds")
    if len(result['Special Numbers']) <= 6:
        print(f"List of special numbers: {', '.join(map(str, result['Special Numbers']))}")
    else:
        print(
            f"Showing first and last 3 special numbers: {', '.join(map(str, result['Special Numbers'][:3] + result['Special Numbers'][-3:]))}")
    print('---')
# eventually remove inputs cuz won't pass hardcode check
