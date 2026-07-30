n = int(input("Enter the number : "))
l = list(map(int, input("Enter the numbers separated by space: ").split()))
def missing_num(n,l):
    total = n * (n + 1) // 2
    sum_of_list = sum(l)
    return total - sum_of_list

print(missing_num(n, l))
