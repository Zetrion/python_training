class queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def overflow(self):
        return len(self.items) >= 10
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty queue")
    

q = queue()

while not q.overflow():
    item = input("Enter an item to enqueue (or type 'exit' to stop): ")
    if item == 'exit':
        break
    q.enqueue(item)

print(q.dequeue())
print(q.is_empty())
print(q.size())
print(q.overflow())