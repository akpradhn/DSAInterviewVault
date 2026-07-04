class Solution:
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 == 1:
            return 0

        subset_sum = (total + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for current_sum in range(subset_sum, num - 1, -1):
                dp[current_sum] += dp[current_sum - num]

        return dp[subset_sum]
