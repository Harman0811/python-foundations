# A tuple is similar to a list, but it is immutable.
# (which means its values cannot be changed after creation).

# Properties of tuples:
# - Ordered
# - Immutable (cannot modify)
# - Allows duplicate values

# Tuples are created using parentheses ()

print(" CREATING A TUPLE ")

numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)


print(" ACCESSING ELEMENTS ")

# indexing starts from 0
print("First element:", numbers[0])
print("Last element:", numbers[-1])


print(" SLICING A TUPLE ")

print("First three elements:", numbers[0:3])
print("From index 2 onwards:", numbers[2:])


print(" TUPLE WITH DIFFERENT DATA TYPES ")

mixed_tuple = (1, "python", 3.14, True)
print("Mixed tuple:", mixed_tuple)


print(" TUPLE PACKING ")

# packing means storing multiple values into a tuple
packed_tuple = 5, 10, 15
print("Packed tuple:", packed_tuple)


print(" TUPLE UNPACKING ")

# unpacking means extracting values from tuple
a, b, c = packed_tuple
print("a =", a)
print("b =", b)
print("c =", c)


print(" COUNT AND INDEX METHODS ")

values = (1, 2, 3, 2, 4, 2)

print("Count of 2:", values.count(2))
print("Index of 3:", values.index(3))


print(" LOOPING THROUGH TUPLE ")

for item in numbers:
    print("Element:", item)


print(" IMPORTANT: TUPLES ARE IMMUTABLE ")

example_tuple = (1, 2, 3)

# Uncommenting the next line will cause an error
# example_tuple[0] = 100

print("Tuples cannot be modified after creation.")

# QUICK SUMMARY:

# () → create tuple
# immutable → cannot change values
# packing → putting values into tuple
# unpacking → extracting values
# count() → count occurrences
# index() → find position