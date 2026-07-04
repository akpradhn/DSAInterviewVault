class Solution:
    def countBits(self, n):
        bits = [0] * (n + 1)

        for value in range(1, n + 1):
            bits[value] = bits[value >> 1] + (value & 1)

        return bits
