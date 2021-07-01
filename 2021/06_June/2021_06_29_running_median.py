import bisect

# O(n log(n)) time complexity:
# -> O(log(n)) time complexity for each insert, n inserts
# -> get median in O(1)
# O(n) space complexity: store all elements from stream
def running_median(stream):
    data = []
    size = 0

    for s in stream:
        bisect.insort(data, s)
        size += 1

        middle = size // 2
        if size % 2 == 0:
            print((data[middle - 1] + data[middle]) / 2)
        else:
            print(data[middle])

running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2
