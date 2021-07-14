class minStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack == []: self.stack.append((x, x))
        else: self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
