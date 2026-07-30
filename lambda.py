
# sq = lambda x: x*x
# print(sq(5))

# n = int(input("Enter the number of elements: "))
# num = [i for i in range(1, n+1)]
# sq = list(map(lambda x: x*x, num))
# print(sq)

n = int(input("Enter the number of elements: "))
num = [i for i in range(1, n+1)]
odd = list(filter(lambda x: x%2!=0, num))
print(odd)