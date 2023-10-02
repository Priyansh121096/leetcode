# https://leetcode.com/problems/min-cost-climbing-stairs/
# 746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        if N == 2:
            return min(cost)
        
        cost.append(0)
        prev, prevprev = cost[1], cost[0]
        for i in range(2, N+1):
            curr = min(prev, prevprev) + cost[i]
            prevprev = prev
            prev = curr
            
        return curr
