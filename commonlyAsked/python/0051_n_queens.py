class Solution:
    def solveNQueens(self, n: int):
        result = []
        board = [["."] * n for _ in range(n)]
        columns = set()
        diagonals = set()
        anti_diagonals = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(current_row) for current_row in board])
                return

            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col
                if col in columns or diagonal in diagonals or anti_diagonal in anti_diagonals:
                    continue

                board[row][col] = "Q"
                columns.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)

                backtrack(row + 1)

                board[row][col] = "."
                columns.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)

        backtrack(0)
        return result
