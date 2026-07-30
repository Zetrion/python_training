# dvisibility by 3 and 5
num = int(input("Enter a number: "))
if num%3 == 0 and num%5 == 0:
    print("FaaH")
elif num%3 == 0:
    print("Fa")
elif num%5 == 0:
    print("aH")
else:
    print(num)    