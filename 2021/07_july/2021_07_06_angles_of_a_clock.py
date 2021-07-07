# O(1) time complexity: simple math
# O(1) space complexity: not much that could take up space
def calcAngle(h, m):
    def hToAngle(h, m = 0):
        return (h % 12 + m / 60) * 30

    def mToAngle(m):
        return m * 6

    angleM, angleH = mToAngle(m), hToAngle(h, m)
    return min(abs(angleM - angleH), 360 - abs(angleH - angleM))

print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
