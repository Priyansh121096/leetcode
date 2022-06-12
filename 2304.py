# https://leetcode.com/problems/minimum-path-cost-in-a-grid/
# 2304. Minimum Path Cost in a Grid

from functools import lru_cache

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        @lru_cache
        def helper(i, j):
            currVal = grid[i][j]
            
            if i == len(grid)-1:
                return currVal
            
            minCost = inf
            for nj in range(len(grid[0])):
                cost = currVal + moveCost[currVal][nj] + helper(i+1, nj)
                minCost = min(minCost, cost)
                
            return minCost
        
        minCost = inf
        for j in range(len(grid[0])):
            cost = helper(0, j)
            minCost = min(minCost, cost)
            
        return minCost