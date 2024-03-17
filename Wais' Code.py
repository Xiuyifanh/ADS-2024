import time


def primic(num):  # Prime number checking
    if num < 2:
        return False
    if num == 2:  # if its 2 return prime
        return True
    if num % 2 == 0:  # if divisible by 2 return false
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):  # range definition
        if num % i == 0:  # divisible by self, return false
            return False
    return True


def palindromic(num):  # string conversion for palindrome
    return str(num) == str(num)[::-1]


def fetch_special_numbers(m, n):
    special_numbers = []
    for number in range(max(2, m), n + 1):
        if primic(number) and palindromic(number):  # if it is prime and palindrome;
            special_numbers.append(number)  # then append to the list
    return special_numbers  # return the fully appended list


def display_numbers(numbers):
    if len(numbers) <= 6:  # display all special numbers if less than six
        return numbers
    else:
        return numbers[:3] + numbers[-3:]  # display first three and last three special numbers


def main():
    m = int(input("Enter the smaller number (m): "))
    n = int(input("Enter the larger number (n): "))

    start_time = time.time()

    special_numbers = fetch_special_numbers(m, n)
    displayed_numbers = display_numbers(special_numbers)

    end_time = time.time()

    print(f"Special numbers between {m} and {n}: {displayed_numbers}")
    print(f"Total special numbers found: {len(special_numbers)}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
