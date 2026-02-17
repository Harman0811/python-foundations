# operators.py
# This file contains practice examples of different types of operators in Python.
# I created this while learning Python fundamentals.

print(" ARITHMETIC OPERATORS ")

a = 15
b = 4

print("a =", a)
print("b =", b)

print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Floor Division (a // b):", a // b)
print("Modulus (a % b):", a % b)
print("Exponent (a ** b):", a ** b)


print(" COMPARISON OPERATORS ")

x = 10
y = 20

print("x =", x)
print("y =", y)

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)


print(" ASSIGNMENT OPERATORS ")

num = 5
print("Initial value:", num)

num += 3   # same as num = num + 3
print("After += 3:", num)

num *= 2   # multiply and assign
print("After *= 2:", num)

num -= 4
print("After -= 4:", num)


print(" LOGICAL OPERATORS")

p = True
q = False

print("p =", p)
print("q =", q)

print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)


print(" MEMBERSHIP OPERATORS ")

fruits = ["apple", "banana", "mango"]

print("Is 'apple' in fruits?", "apple" in fruits)
print("Is 'grape' not in fruits?", "grape" not in fruits)


print(" IDENTITY OPERATORS ")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)      # True (same memory)
print("list1 is list3:", list1 is list3)      # False (different objects)
print("list1 == list3:", list1 == list3)      # True (same values)
