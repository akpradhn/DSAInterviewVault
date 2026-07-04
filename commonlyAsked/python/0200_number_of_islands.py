class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def sink(row, col):
            if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != "1":
                return

            grid[row][col] = "0"
            sink(row - 1, col)
            sink(row + 1, col)
            sink(row, col - 1)
            sink(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    sink(row, col)

        return islands
