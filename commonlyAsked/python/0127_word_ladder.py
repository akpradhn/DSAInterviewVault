class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if beginWord == endWord:
            return 1

        unvisited = set(wordList)
        if endWord not in unvisited:
            return 0

        queue = [(beginWord, 1)]
        head = 0
        unvisited.discard(beginWord)

        while head < len(queue):
            word, distance = queue[head]
            head += 1
            chars = list(word)

            for i in range(len(chars)):
                original = chars[i]
                for code in range(97, 123):
                    replacement = chr(code)
                    if replacement == original:
                        continue

                    chars[i] = replacement
                    next_word = "".join(chars)
                    if next_word == endWord:
                        return distance + 1
                    if next_word in unvisited:
                        unvisited.remove(next_word)
                        queue.append((next_word, distance + 1))

                chars[i] = original

        return 0
