class Solution:
    def coinChange(self, coins, amount):
        impossible = amount + 1
        dp = [impossible] * (amount + 1)
        dp[0] = 0

        for total in range(1, amount + 1):
            for coin in coins:
                if coin <= total:
                    candidate = dp[total - coin] + 1
                    if candidate < dp[total]:
                        dp[total] = candidate

        if dp[amount] == impossible:
            return -1
        return dp[amount]
