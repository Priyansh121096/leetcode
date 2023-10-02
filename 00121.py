# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        maxProfit = 0
        sell = N-1
        for buy in range(N-2, -1, -1):
            if prices[buy] >= prices[sell]:
                sell = buy
            else:
                profit = prices[sell] - prices[buy]
                maxProfit = max(profit, maxProfit)
                
        return maxProfit
