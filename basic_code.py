# Take a number from user and print whether it is:
num = int(input("enter a number: "))
print("entered number is : ", num, "which is of type", type(num))

# Swap two numbers without using third variable.
a = 12
b = 54

print(f"before swaping: a : {a}  b : {b}")

temp = a
a = b
b = temp
print(f"after swaping : a : {a} b : {b}")

# Print sum of first 100 natural numbers.
sum = 0
for i in range(101):
    sum = sum + i

# print("sum of first 100 natural numbers is :", sum)

# Reverse a number (e.g., 123 → 321).
num = num = input("Enter a number: ")
print("number is : ", num)

reverse = num[::-1]
print("Reversed number:", reverse)


# Count how many vowels are in a string.
text = "hey I am coding in VS code and this program is used to count the no. of vowels in a string"
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

# print("Total number of vowels in the given string is:", count)

