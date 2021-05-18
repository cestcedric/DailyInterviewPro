# All actions in time complexity O(1)
# Space complexity O(2*n), as we save the current max with each value
class MaxStack1:
    def __init__(self):
        self.data = []
        self.size = 0


    def push(self, val):
        # empty stack
        if self.size == 0: self.data.append((val, val))
        # stack filled, new value is new maximum
        elif val > self.data[0][1]: self.data.append((val, val))
        else: self.data.append((val, self.data[-1][1]))
        self.size += 1


    def pop(self):
        if self.size == 0: return None
        self.size -= 1
        return self.data.pop(-1)[0]


    def max(self):
        return self.data[-1][1]

# All actions in time complexity O(1)
# Space complexity between O(n) and O(2*n), depending on how often the max value increases
class MaxStack2:
    def __init__(self):
        self.data = []
        self.size = 0
        self.maxIndex = []


    def push(self, val):
        if self.size == 0:
            self.maxIndex = [0]
        elif val > self.data[self.maxIndex[-1]]:
            self.maxIndex.append(self.size)
        self.data.append(val)
        self.size += 1


    def pop(self):
        if self.size == 0: return None
        if self.size == self.maxIndex[-1] + 1:
            self.maxIndex = self.maxIndex[:-1]
        self.size -= 1
        return self.data.pop(-1)
        

    def max(self):
        return self.data[self.maxIndex[-1]]

s = MaxStack1()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print('Should be 3: {}'.format(s.max()))
s.pop()
s.pop()
print('Should be 2: {}'.format(s.max()))
s = MaxStack2()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print('Should be 3: {}'.format(s.max()))
s.pop()
s.pop()
print('Should be 2: {}'.format(s.max()))

