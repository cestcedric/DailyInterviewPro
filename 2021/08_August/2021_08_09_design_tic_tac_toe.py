from collections import defaultdict

class TicTacToe(object):
    # O(n^2) time: building lists for board
    # O(n^2) space
    def __init__(self, n):
        self.size = n

        # for printing
        self.board = [[' '] * n for _ in range(n)]
        self.players = ['X', 'O']

        # record moves in dict for easy win check
        self.rowsP1 = defaultdict(list)
        self.colsP1 = defaultdict(list)
        self.diagsP1 = defaultdict(list)

        self.rowsP2 = defaultdict(list)
        self.colsP2 = defaultdict(list)
        self.diagsP2 = defaultdict(list)

        # block game if won
        self.decided = False


    # O(1) time: only valid moves played, checking would be O(n)
    # O(n) space: after n moves the dicts for each player will store n new entries
    def move(self, row, col, player):
        if self.decided:
            print('Game over!')
            return

        # check for illegal move not necessary according to description
        self.board[row][col] = self.players[player - 1]
        roundRows = self.rowsP1 if player == 1 else self.rowsP2
        roundCols = self.colsP1 if player == 1 else self.colsP2
        roundDiags = self.diagsP1 if player == 1 else self.diagsP2

        roundRows[row].append(col)
        roundCols[col].append(row)
        if row == col: roundDiags['bottomLeftTopRight'].append(row)
        elif row + col == self.size - 1: roundDiags['topLeftBottomRight'].append(row)

        self.checkWin(row, col, player)

        # for printing
        return self  


    # O(1) time: only checking lengths in player dicts
    # O(1) space: no additional space used
    def checkWin(self, row, col, player):
        roundRows = self.rowsP1 if player == 1 else self.rowsP2
        roundCols = self.colsP1 if player == 1 else self.colsP2
        roundDiags = self.diagsP1 if player == 1 else self.diagsP2
        
        self.decided |= len(roundRows[row]) == self.size
        self.decided |= len(roundCols[col]) == self.size

        if row == col: 
            self.decided |= len(roundDiags['topLeftBottomRight']) == self.size
        elif row + col == self.size - 1:
            self.decided |= len(roundDiags['topLeftBottomRight']) == self.size

        if self.decided:
            print('Player {} won!'.format(player))


    def __str__(self) -> str:
        string = ''
        for row in self.board:
            string += '|'
            for field in row:
                string += ' {} |'.format(field)
            string += '\n'
        return string

    
board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))
board.move(1, 2, 2)
