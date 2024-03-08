import time


def is_palindrome(n):
    num = n
    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num //= 10
    return n == reverse



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


var_m = int(input("Enter the small number: "))
var_n = int(input("Enter the large number: "))

pali_list = []
start = time.time()

if var_n <= 2:
    pali_list.append(2)
    var_n = 3

if var_n % 2 == 0:
    var_n = var_n + 1

for i in range(var_m, var_n + 1, 2):
    if is_palindrome(i) and is_prime(i):
        pali_list.append(i)

end = time.time()

print("Total time taken: ", end - start)
print("Total special number: ", len(pali_list))

if len(pali_list) < 6:
    print(pali_list)
else:
    print(f"First three Palindromic Prime numbers: {pali_list[:3]}")
    print(f"Last three Palindromic Prime numbers: {pali_list[-3:]}")
