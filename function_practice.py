# Check if Palindrome
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("radar"))  # Output: True
# print(is_palindrome("python"))  # Output: False

'''Write a function:
    get_high_performers
    It should:
        take a list of CGPAs
        take a threshold
        return a list of CGPAs above the threshold'''
def get_high_performers(cgpas, threshold):
    high_performers = []
    for cgpa in cgpas:
        if cgpa > threshold:
            high_performers.append(cgpa)

    return high_performers

cgpas = [ 5.66, 7.9, 7.99, 6.89, 9.8, 8.9, 8.4]

result = get_high_performers(cgpas, 8.0)

if not result:
    print("List is empty!!!!!")
else:
    print(result)