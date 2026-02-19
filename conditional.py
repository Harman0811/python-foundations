# Check whether a number is even or odd

num = int(input("enter a number : "))

if (num < 0):
    print("negetive number")
elif (num == 0):
    print("zero entered")
elif (num % 2 == 0):
    print("even number")
else :
    print("odd number")

# Find the largest of two numbers
a = int(input("Enter first digit: "))
b = int(input("Enter second digit: "))

if a > b:
    print("First number is greater:", a)
elif b > a:
    print("Second number is greater:", b)
else:
    print("Both numbers are equal")


# Take a number and print: "Even and divisible by 4","Even but not divisible by 4","Odd"
n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Odd number")
elif n % 4 == 0:
    print("Even and divisible by 4")
else:
    print("Even but not divisible by 4")

# Rock-Paper-Scissors (user vs computer logic only, no random yet)
user = input("Enter rock, paper, or scissors: ").lower()
computer = "rock"   # fixed choice for now

if user == computer:
    print("It's a tie!")

elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You win!")

elif user in ["rock", "paper", "scissors"]:
    print("Computer wins!")

else:
    print("Invalid input")
