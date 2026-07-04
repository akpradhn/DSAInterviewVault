class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        if len(word) > rows * cols:
            return False

        board_counts = {}
        for row in board:
            for char in row:
                board_counts[char] = board_counts.get(char, 0) + 1

        word_counts = {}
        for char in word:
            word_counts[char] = word_counts.get(char, 0) + 1

        for char, needed in word_counts.items():
            if board_counts.get(char, 0) < needed:
                return False

        if board_counts.get(word[0], 0) > board_counts.get(word[-1], 0):
            word = word[::-1]

        def dfs(row, col, index):
            if board[row][col] != word[index]:
                return False
            if index == len(word) - 1:
                return True

            current = board[row][col]
            board[row][col] = None

            next_index = index + 1
            found = (
                row > 0 and dfs(row - 1, col, next_index)
                or row + 1 < rows and dfs(row + 1, col, next_index)
                or col > 0 and dfs(row, col - 1, next_index)
                or col + 1 < cols and dfs(row, col + 1, next_index)
            )

            board[row][col] = current
            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
