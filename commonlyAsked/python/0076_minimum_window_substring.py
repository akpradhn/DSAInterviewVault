class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        missing = len(t)
        left = 0
        best_start = 0
        best_length = len(s) + 1

        for right, char in enumerate(s):
            if char in need:
                if need[char] > 0:
                    missing -= 1
                need[char] -= 1

            while missing == 0:
                window_length = right - left + 1
                if window_length < best_length:
                    best_start = left
                    best_length = window_length

                left_char = s[left]
                if left_char in need:
                    need[left_char] += 1
                    if need[left_char] > 0:
                        missing += 1
                left += 1

        if best_length == len(s) + 1:
            return ""
        return s[best_start:best_start + best_length]
