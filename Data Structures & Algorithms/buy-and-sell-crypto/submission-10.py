class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            min_price = min(prices[i],min_price)
            max_price = max(profit, max_price)
        return max_price
