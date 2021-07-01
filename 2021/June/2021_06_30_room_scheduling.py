import heapq

# O(n^2) time complexity: if all events at the same time, we check k - 1 rooms for event k
# O(n) space complexity: at most n rooms
def scheduling(events: list) -> int:
    events.sort(key = lambda event : event[0])
    rooms, r = [events[0]], 1

    for event in events[1:]:
        scheduled = False
        for i in range(r):
            if rooms[i][1] <= event[0]:
                rooms[i] = event
                scheduled = True 
                break
        if not scheduled:
            rooms.append(event)
            r += 1

    return r
            

# O(n * log(n)) time complexity: heappush in O(log(n)), happens O(n) times
# O(n) space complexity: heap with at most n elements
def schedulingHeap(events: list) -> int:
    if events == []: return 0
    events.sort(key = lambda event : event[0])
    
    heap = [events[0][::-1]]
    for event in events[1:]:
        prev = heapq.heappop(heap)
        if prev[0] <= event[0]:
            heapq.heappush(heap, event[::-1])
        else:
            heapq.heappush(heap, prev)
            heapq.heappush(heap, event)

    return len(heap)


print('Should be 2:', schedulingHeap([[0, 30],[5, 10],[15, 20]]))
print('Should be 2:', schedulingHeap([(30, 75), (0, 50), (60, 150)]))
print('Should be 1:', schedulingHeap([[7,10],[2,4]]))