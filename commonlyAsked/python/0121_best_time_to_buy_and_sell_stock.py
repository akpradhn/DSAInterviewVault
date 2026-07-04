class Solution:
    def maxProfit(self, prices):
        best_buy = prices[0]
        best_profit = 0

        for price in prices[1:]:
            if price < best_buy:
                best_buy = price
            else:
                best_profit = max(best_profit, price - best_buy)

        return best_profit
