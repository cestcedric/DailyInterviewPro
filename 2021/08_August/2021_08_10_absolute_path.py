# O(n) time
# O(n) space
# Assumes a complete path, with leading / and .. only after a named component
def shortest_path(file_path):
    file_path = file_path.split('/')
    simplified_path = []

    for x in file_path:
        if x == '.': continue
        if x == '..': simplified_path.pop()
        else: simplified_path.append(x)

    return '/'.join(simplified_path)

print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/
