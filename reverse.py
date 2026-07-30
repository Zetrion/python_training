# reverse a number using recursion
integer = int(input("Enter a number: "))

def reverse_number(n):
    if n < 10:
        return n
    else:
        return int(str(n)[-1] + str(reverse_number(n // 10)))

print(reverse_number(integer))