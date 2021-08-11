# O(n) time
# O(n) space
# Handles .. leading to root as well as multiple ///
def shortest_path(file_path):
    file_path = file_path.split('/')
    simplified_path = []

    for x in file_path:
        if x == '.': continue
        if x == '..':
            if simplified_path != []: simplified_path.pop()
        else: simplified_path.append(x)

    return '/' + '/'.join(simplified_path)

print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/
