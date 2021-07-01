# O(n log(n)) time complexity due to sorting
# O(n) for sorted_intervals (not necessary if sorted in place)
def merge(intervals):
    if intervals == []: return []
    sorted_intervals = sorted(intervals, key = lambda x: x[0])
    merged = [sorted_intervals[0]]
    for i in sorted_intervals[1:]:
        if merged[-1][1] < i[0]: merged.append(i)
        else: merged[-1] = merged[-1][0], max(merged[-1][1], i[1]) # Tuple item assignment not supported in python 3.7
    return merged

  
print('Should be:\n[(1, 3), (4, 10), (20, 25)]\n{}'.format(merge([(1, 3), (5, 8), (4, 10), (20, 25)])))
print('Should be:\n[(1, 10)]\n{}'.format(merge([[2,3],[4,5],[6,7],[8,9],[1,10]])))
