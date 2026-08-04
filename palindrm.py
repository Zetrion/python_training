n = input("Enter a string: ")
def is_palindrome(n):
    length = len(n)
    for i in range(length // 2):
        if n[i] != n[length - 1 - i]:
            return False
    return True

if is_palindrome(n):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")