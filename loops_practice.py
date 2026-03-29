# print numbers from 1 to N
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(i)

# sum of first N natural numbers
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)

# multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# count digits in a number
num = int(input("Enter a number: "))
count = 0

if num == 0:
    count = 1

while num != 0:
    num //= 10
    count += 1

print("Total digits:", count)

# reverse a number
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)

# check prime number
num = int(input("Enter a number: "))

if num <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not prime")

# fibonacci series
n = int(input("Enter number of terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# sum of digits
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)

# count vowels in a string
text = input("Enter a string: ").lower()
count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)