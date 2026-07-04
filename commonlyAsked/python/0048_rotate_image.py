class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(n):
            left = 0
            right = n - 1
            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1
