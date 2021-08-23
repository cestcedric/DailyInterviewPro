from collections import Counter
from heapq import heappop, heappush

# O(n * log(n)) time complexity: n = number of different activities, [1,1,2] => n = 2
# O(n) space: heap with n entries
# not only computes the number of total duration but can return schedule
def findTime(arr, cooldown):
    if cooldown == 0: return len(arr)

    # highest frequency activity has to be started first
    activityCounts = Counter(arr)

    totalTime = 0
    totalActivities = 0
    readyHeap = []
    busyHeap = []

    for a in activityCounts:
        # negate because heap returns min element
        heappush(readyHeap, (-activityCounts[a], a))

    while totalActivities < len(arr):
        if len(readyHeap) > 0:
            count, activity = heappop(readyHeap)
            heappush(busyHeap, (totalTime + cooldown + 1, count + 1, activity))
            totalActivities += 1

        totalTime += 1

        if len(busyHeap) > 0 and busyHeap[0][0] == totalTime:
            _, count, activity = heappop(busyHeap)
            if count < 0: heappush(readyHeap, (count, activity))

    return totalTime


# O(n) time
# O(1) space
# cooldown gaps long enough to fill up => most frequent activities determine length
# cooldown gaps too short => can always work => number of activities = time
def findTimeMath(arr, cooldown):
    activityCounts = Counter(arr)
    maxCount = max(activityCounts.values())
    maxActivitiesCount = list(activityCounts.values()).count(maxCount)
    return max(len(arr), (maxCount - 1) * (cooldown + 1) + maxActivitiesCount)



print('Should be 7:', findTimeMath([1, 1, 2, 1], 2))
print('Should be 8:', findTimeMath([1, 1, 1, 2, 2, 2], 2))
print('Should be 6:', findTimeMath([1, 1, 1, 2, 2, 2], 1))
print('Should be 16:', findTimeMath([1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7], 2))
print('Should be 1:', findTimeMath([1], 2))

