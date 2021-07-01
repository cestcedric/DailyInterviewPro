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
            

print('Should be 2:', scheduling([[0, 30],[5, 10],[15, 20]]))
print('Should be 2:', scheduling([(30, 75), (0, 50), (60, 150)]))
print('Should be 1:', scheduling([[7,10],[2,4]]))