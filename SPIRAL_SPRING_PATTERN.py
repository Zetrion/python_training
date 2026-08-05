string = input("Enter a string: ")
for i in range(len(string)):
    print(string[0:len(string)-i], end= " ")