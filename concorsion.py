r = input("Enter a string: ")
emp = ""
count = 1
for i in range(len(r)-1):
    if r[i] == r[i+1]:
        count += 1
    else:
        emp += r[i] + str(count)
        count = 1
        
emp+= r[-1] + str(count)
print(emp)        