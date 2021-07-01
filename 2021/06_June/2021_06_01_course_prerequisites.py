def courses_to_take(course_to_prereqs):
    # O(n^2) time complexity
    # Worst case there is one order where all courses have at least one more prereq than the previous one
    # O(n) space complexity
    attended = {}
    todo = {}
    for course in course_to_prereqs:
        if course_to_prereqs[course] == []: attended[course] = True
        else: todo[course] = True

    changed = True
    while changed:
        done = []
        changed = False
        for course in todo:
            cleared = True
            for pre in course_to_prereqs[course]:
                if pre not in attended and pre not in todo: 
                    todo[pre] = True
                    cleared = False
                    changed = True
                elif pre not in attended:
                    cleared = False
            if cleared:
                done.append(course)
                attended[course] = True
                changed = True
        for course in done: del(todo[course])

    if list(todo.keys()) != []: return None
    else: return [ course for course in attended.keys() ]



courses = {
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'], 
    'CSC100': []
}
print('Should be\n[\'CSC100\', \'CSC200\', \'CSC300\']:\n{}'.format(courses_to_take(courses)))
print('-'*10)

courses = {
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'], 
    'CSC100': ['CSC200']
}
print('Should be None:\n{}'.format(courses_to_take(courses)))
print('-'*10)

courses = {
    'CSC400': ['CSC200'],
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'], 
    'CSC100': []
}
print('Should be\n[\'CSC100\', \'CSC200\', \'CSC300\', \'CSC400\'] or\n[\'CSC100\', \'CSC200\', \'CSC400\', \'CSC300\']:\n{}'.format(courses_to_take(courses)))
print('-'*10)
