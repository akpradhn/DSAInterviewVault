class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for start_row in range(rows):
            for start_col in range(cols):
                if memo[start_row][start_col] != 0:
                    continue

                stack = [(start_row, start_col, False)]
                while stack:
                    row, col, ready = stack.pop()
                    if memo[row][col] != 0:
                        continue

                    if ready:
                        best = 1
                        value = matrix[row][col]
                        for row_delta, col_delta in directions:
                            next_row = row + row_delta
                            next_col = col + col_delta
                            if (
                                0 <= next_row < rows
                                and 0 <= next_col < cols
                                and matrix[next_row][next_col] > value
                            ):
                                best = max(best, 1 + memo[next_row][next_col])
                        memo[row][col] = best
                    else:
                        stack.append((row, col, True))
                        value = matrix[row][col]
                        for row_delta, col_delta in directions:
                            next_row = row + row_delta
                            next_col = col + col_delta
                            if (
                                0 <= next_row < rows
                                and 0 <= next_col < cols
                                and matrix[next_row][next_col] > value
                                and memo[next_row][next_col] == 0
                            ):
                                stack.append((next_row, next_col, False))

        longest = 0
        for row in range(rows):
            for col in range(cols):
                longest = max(longest, memo[row][col])

        return longest
