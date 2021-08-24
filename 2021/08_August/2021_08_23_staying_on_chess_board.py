# O(1) time
def getMoves(x: int, y: int) -> list:
    moves = [(2, 1), (2, -1), (1, 2), (1, -2)]
    positions = []
    for a, b in moves:
        positions.append((x + a, y + b))
        positions.append((x - a, y - b))
    return positions

# O(1) time
def checkInbound(x: int, y: int, BOARDSIZE = 8) -> bool:
    return (-1 < x < BOARDSIZE and -1 < y < BOARDSIZE)


# O(8^k) time: for infinitely big chess board, with no cache kicking in
# O(8^k) space: cache
def is_knight_on_board_rec(x: int, y: int, k: int, cache={}) -> float:
    if (x, y, k) in cache: return cache[(x, y, k)]

    if k == 0: return 1

    pOnBoard = 0
    for newX, newY in getMoves(x, y):
        if checkInbound(newX, newY):
            pOnBoard += 1 / 8 * is_knight_on_board(newX, newY, k - 1, cache)

    cache[(x, y, k)] = pOnBoard
    return pOnBoard


# O(n^2 * k) time: n = side length of board
# O(n^2) space: need space to save two complete boards
def is_knight_on_board(x: int, y: int, k: int) -> float:
    if k == 0: return 1
    BOARDSIZE = 8
    
    board1 = [[0] * BOARDSIZE for _ in range(BOARDSIZE)]
    board1[x][y] = 1

    for _ in range(k):
        board2 = [[0] * BOARDSIZE for _ in range(BOARDSIZE)]
        for x in range(BOARDSIZE):
            for y in range(BOARDSIZE):
                if board1[x][y] == 0: continue
                for newX, newY in getMoves(x, y):
                    if checkInbound(newX, newY, BOARDSIZE):
                        board2[newX][newY] += board1[x][y] / 8
        
        board1 = board2

    return sum(sum(row) for row in board2)





print(is_knight_on_board(0, 0, 1))
# 0.25
