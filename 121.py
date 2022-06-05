# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        buy, sell = N-2, N-1
        mp = 0
        while buy >= 0:
            if prices[buy] > prices[sell]:
                sell = buy
                
            else:
                profit = prices[sell] - prices[buy]
                mp = max(mp, profit)
            buy -= 1
            
        return mp   