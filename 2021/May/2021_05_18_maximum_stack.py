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


class MaxStack2:
    def __init__(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def max(self):
        pass

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

