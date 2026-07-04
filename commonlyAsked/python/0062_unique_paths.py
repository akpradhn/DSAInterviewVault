class Solution:
    def uniquePaths(self, m, n):
        row = [1] * n

        for _ in range(1, m):
            for col in range(1, n):
                row[col] += row[col - 1]

        return row[n - 1]
