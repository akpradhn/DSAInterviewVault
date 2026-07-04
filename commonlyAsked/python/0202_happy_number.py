class Solution:
    def isHappy(self, n):
        def next_number(value):
            total = 0
            while value:
                digit = value % 10
                total += digit * digit
                value //= 10
            return total

        slow = n
        fast = next_number(n)

        while fast != 1 and slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return fast == 1
