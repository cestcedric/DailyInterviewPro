def word_search(matrix, word):
    # Time complexity O(n*m*w) with n*m matrix entries and word length w
    x_range = len(matrix)
    y_range = len(matrix[0])
    w_len = len(word)
    for x in range(x_range):
        for y in range(y_range):
            if matrix[x][y] == word[0]:
                i = 1
                # check left-to-right
                while i < w_len and i + y < y_range:
                    if matrix[x][y+i] != word[i]: break
                    i += 1
                if i == w_len: return True
                # check top-to-bottom
                while i < w_len and i + x < x_range:
                    if matrix[x+i][y] != word[i]: break
                    i += 1
                if i == w_len: return True
    return False
                

  
  
matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print('Should be \'True\': {}'.format(word_search(matrix, 'FOAM')))
print('Should be \'False\': {}'.format(word_search(matrix, 'STAR')))
