class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 1e4
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > profit:
                profit = prices[i] -minprice
        return profit
