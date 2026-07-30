# palindrome
i = input("Enter a string: ")
str_i = str(i)
if str_i == str_i[::-1]:
    print("True")
else:
    print("False")
