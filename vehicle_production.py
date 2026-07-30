v = int(input("Enter the number of vehicles produced: "))
w = int(input("Enter the number of wheels produced: "))

if w % 2 != 0 or w < 2 * v or w > 4 * v:
    print("INVALID INPUT")
    
y=(w-2*v)/2
x=v-y
print(f"Number of cars: {x}")
print(f"Number of motorcycles: {y}")

# x + y = v
# 2x + 4y = w
# y = (w -2x)/4
# x = v - y
# y = (w - 2*v)/2