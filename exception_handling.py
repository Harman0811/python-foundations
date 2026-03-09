# Exception Handling Practice

print("Example 1: Handling division error")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please enter a valid number.")

print("\nExample 2: Using else block")

try:
    number = int(input("Enter another number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", number)


print("\nExample 3: Using finally block")

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File does not exist.")

finally:
    print("This block always runs.")


print("\nExample 4: Multiple operations with error handling")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Division result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

print("\nProgram finished.")