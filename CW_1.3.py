import time


def is_palindrome(n, lower_bound, upper_bound):
    if lower_bound <= n <= upper_bound:
        num = n
        reverse = 0
        while num > 0:
            last_digit = num % 10
            reverse = reverse * 10 + last_digit
            num //= 10
        return n == reverse
    else:
        return False


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


var_m = int(input("Enter the small number: "))
var_n = int(input("Enter the large number: "))

pali_list = []
start = time.time()

for i in range(max(2, var_m), var_n + 1):  # Adjusting the range to ensure 2 is included if applicable
    if is_palindrome(i, var_m, var_n) and is_prime(i):
        pali_list.append(i)

end = time.time()

print("Total time taken: ", end - start)
print("Total special number: ", len(pali_list))

if len(pali_list) < 6:
    print(pali_list)
else:
    print(f"First three Palindromic Prime numbers: {pali_list[:3]}")
    print(f"Last three Palindromic Prime numbers: {pali_list[-3:]}")
