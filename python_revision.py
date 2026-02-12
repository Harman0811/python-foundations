'''''Stores a students name, age, CGPA
    Calculates CGPA after adding 0.3 bonus'''

# name = input("Enter the student name: ")
# age = int(input("Enter the age: "))
# cgpa = float(input("enter the cgpa of student: "))

# BONUS_CGPA = 0.3

# updated_cgpa = cgpa + BONUS_CGPA

# print(f"Name : {name}")
# print(f"Age : {age}")
# print(f"cgpa : {updated_cgpa:.2f}")

cgpas = [9.9, 6.9, 7.8, 9.0, 7.2]
# total = sum(cgpas)
# count = len(cgpas)

# average = total / count

# print(f"Average cgpa : {average:.2f}")

for item in cgpas :
    if (item > 8.0) :
        print(item)