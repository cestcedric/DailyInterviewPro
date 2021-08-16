# this is literally the same problem as 2021_0813_spreadsheet_column_title
# O(n) time: n = length of title
# O(1) space: only space for output string needed
def column_name(n):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    title = ''

    while n > 0:
        n, m = divmod(n, 26)
        title += ALPHABET[m]
        if m == 0: n -= 1

    return title[::-1]


print(column_name(26))
print(column_name(27))
print(column_name(28))
# Z
# AA
# AB
