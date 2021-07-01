def distance(s1, s2):
    # Edit distance also known as Levenshtein Distance
    # Dynamic programmin approach with time and space complexity O(len(s1)*len(s2))
    l1 = len(s1) + 1
    l2 = len(s2) + 1
    matrix = [ [ 0 for _ in range(l2) ] for _ in range(l1) ]

    for x in range(l1):
        for y in range(l2):
            if y == 0: matrix[x][y] = x
            elif x == 0: matrix[x][y] = y
            else:
                if s1[x-1] == s2[y-1]:
                    matrix[x][y] = min(
                        matrix[x-1][y] + 1,
                        matrix[x-1][y-1],
                        matrix[x][y-1] + 1
                    )
                else:
                    matrix[x][y] = min(
                        matrix[x-1][y] + 1,
                        matrix[x-1][y-1] + 1,
                        matrix[x][y-1] + 1
                    )
    return matrix[-1][-1]


def distanceSmol(s1, s2):
    # Same time complexity O(len(s1)*len(s2))
    # Space complexity reduced to O(2*len(s2))
    # For maximum optimization choose the shorter string as l2
    l1 = len(s1) + 1
    l2 = len(s2) + 1
    matrix = [ [ 0 for _ in range(l2) ] for _ in range(2) ]

    for x in range(l1):
        _x = x % 2
        for y in range(l2):
            if y == 0: matrix[_x][y] = x
            elif x == 0: matrix[_x][y] = y
            else:
                if s1[x-1] == s2[y-1]:
                    matrix[_x][y] = min(
                        matrix[_x-1][y] + 1,
                        matrix[_x-1][y-1],
                        matrix[_x][y-1] + 1
                    )
                else:
                    matrix[_x][y] = min(
                        matrix[_x-1][y] + 1,
                        matrix[_x-1][y-1] + 1,
                        matrix[_x][y-1] + 1
                    )
    return matrix[_x][-1]

         
print('Should be 2: {}'.format(distance('biting', 'sitting')))
print('Should be 2: {}'.format(distanceSmol('biting', 'sitting')))
