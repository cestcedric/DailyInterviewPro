# O(n) time complexity: look at each entry once
# O(1) space complexity when directly printing instead of adding to 'output'
# here obviously O(n) space complexity, since saving results in list
def matrix_spiral_print(M):
    height, width = len(M), len(M[0])
    up_l, up_r = (0, 0), (0, width-1)
    lo_l, lo_r = (height-1, 0), (height-1, width-1)
    output = []

    while up_l[0] <= lo_l[0] and up_l[1] <= up_r[1]:
        x, y = up_l
        while y <= up_r[1]: 
            output.append(M[x][y])
            y += 1

        x, y = up_r
        x += 1
        while x <= lo_r[0]: 
            output.append(M[x][y])
            x += 1

        if up_r == lo_r or lo_r == lo_l: break

        x, y = lo_r
        y -= 1
        while y >= lo_l[1]:
            output.append(M[x][y])
            y -= 1

        x, y = lo_l
        x -= 1
        while x > up_l[0]:
            output.append(M[x][y])
            x -= 1

        up_l = up_l[0]+1, up_l[1]+1
        up_r = up_r[0]+1, up_r[1]-1
        lo_l = lo_l[0]-1, lo_l[1]+1
        lo_r = lo_r[0]-1, lo_r[1]-1

    print(' '.join([ str(o) for o in output ]))


grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
print('Should be:\n1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12')
matrix_spiral_print(grid)


grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print('Should be:\n1 2 3 6 9 8 7 4 5')
matrix_spiral_print(grid)


grid = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
print('Should be:\n1 2 3 4 8 12 11 10 9 5 6 7')
matrix_spiral_print(grid)


grid = [[3],
        [2]]
print('Should be:\n3 2')
matrix_spiral_print(grid)


grid = [[7],
        [9],
        [6]]
print('Should be:\n7 9 6')
matrix_spiral_print(grid)
