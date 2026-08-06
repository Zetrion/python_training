from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}. Queue state: {list(self.queue)}")
        
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.popleft()
            print(f"Dequeued: {item}. Queue state: {list(self.queue)}")
            return item
        else:
            raise IndexError("Dequeue from an empty queue")
        
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from an empty queue")
        
q = Queue()
q.enqueue(1)
q.enqueue(2)    
q.enqueue(3)
print(q.dequeue())
print(q.is_empty())        