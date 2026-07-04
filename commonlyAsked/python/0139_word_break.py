class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        lengths = set()
        for word in words:
            lengths.add(len(word))

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for end in range(1, len(s) + 1):
            for length in lengths:
                start = end - length
                if start >= 0 and dp[start] and s[start:end] in words:
                    dp[end] = True
                    break

        return dp[len(s)]
