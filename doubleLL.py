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
a.prev = head
current = head
while current is not None:
    print(current.data,end="<->")
    current = current.next
    if current is None:
        print("None") 
        
def insert_at_beginning(head, data):
    new_node = linkNode(data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    head = new_node
    return head        
    