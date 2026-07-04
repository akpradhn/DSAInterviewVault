class Solution:
    def longestConsecutive(self, nums):
        values = set(nums)
        longest = 0

        for num in values:
            if num - 1 not in values:
                current = num
                length = 1

                while current + 1 in values:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

