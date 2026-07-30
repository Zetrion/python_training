# josephus problem implementation in Python
n = int(input("Enter the number of people in the circle: "))

def josephus(n):
    return 2 * (n - (1 << (n.bit_length() - 1))) + 1

result = josephus(n)
print(f"The person at position {result} survives")
