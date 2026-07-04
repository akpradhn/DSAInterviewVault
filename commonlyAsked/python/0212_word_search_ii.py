class Solution:
    def findWords(self, board, words):
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["#"] = word

        rows = len(board)
        cols = len(board[0]) if rows else 0
        result = []

        def dfs(row, col, node):
            char = board[row][col]
            if char not in node:
                return

            next_node = node[char]
            word = next_node.pop("#", None)
            if word is not None:
                result.append(word)

            board[row][col] = "#"
            if row > 0:
                dfs(row - 1, col, next_node)
            if row + 1 < rows:
                dfs(row + 1, col, next_node)
            if col > 0:
                dfs(row, col - 1, next_node)
            if col + 1 < cols:
                dfs(row, col + 1, next_node)
            board[row][col] = char

            if not next_node:
                node.pop(char)

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie)

        return result
