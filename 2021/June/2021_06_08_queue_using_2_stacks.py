class Queue:
    def __init__(self):
        self.size = 0
        self.stack1 = []
        self.stack2 = []
        
    # O(1) time complexity
    def enqueue(self, val):
        self.stack1.append(val)
        self.size += 1

    # O(n) time complexity: move whole stack1 to stack2 and back
    def dequeue(self):
        if self.size == 0: return None
        self.size -= 1
        for _ in range(self.size):
            self.stack2.append(self.stack1.pop())
        ret = self.stack1.pop()
        for _ in range(self.size):
            self.stack1.append(self.stack2.pop())
        return ret

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
