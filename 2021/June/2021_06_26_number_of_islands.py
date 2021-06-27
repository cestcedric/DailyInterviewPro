class Solution(object):
    # O(n*m) time complexity: n = rows, m = cols, multiple passes but check for islandId 
    # avoid multiple traversals starting from the same point
    # O(n*m) space complexity: maximum callstack depth when all entries form one big island
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        islandId = 2

        def traverse(x, y):
            nonlocal rows, cols, grid, islandId
            if x in [-1, rows] or y in [-1, cols]: return False
            if grid[x][y] == 1:
                grid[x][y] = islandId
                for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    traverse(i, j)
                return True
            return False

        for r in range(rows):
            for c in range(cols):
                islandId += traverse(r, c)

        return islandId - 2

        


grid = [
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,0,1,0],
    [0,0,0,0,0]]
print(Solution().numIslands(grid))
