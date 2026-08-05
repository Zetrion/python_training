class linkNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

a, b, c, d, e = [linkNode(i) for i in range(1, 11, 2)]
head = linkNode(0, a)

a.next = b
b.next = c
c.next = d
d.next = e
e.prev = d
d.prev = c
c.prev = b
b.prev = a



# while head is not None:
#     print(head.data,end="->")
#     head = head.next
#     if head is None:
#         print("None")
        
for i in range(5):
    n = int(input("Enter a number to check: "))   
    current = head
    found = False
    
    while current is not None:
        if current.data == n:
            found = True
            break
        current = current.next      
    if found:
        print(f"{n} is present in the linked list.")
    else:
        print(f"{n} is not present in the linked list.")
