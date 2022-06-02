# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
# 1039. Minimum Score Triangulation of Polygon

from typing import List
inf, ninf = float('inf'), float('-inf')

# Solution 1
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        if len(values) < 3:
            # So that any invalid polygons are automatically left out.
            return inf 
        
        if len(values) == 3:
            # We already know a triangle's miniumum triangualtion score.
            return values[0]*values[1]*values[2]
        
        mts = inf  # Minimum triangulation score
        for i in range(len(values)-2):
            for j in range(i+2, len(values)):
                # i, j is the side we're picking in this iteration.
                
                # (0, N-1) can't be a side.
                if i == 0 and j == len(values)-1:
                    continue
                 
                fhs = self.minScoreTriangulation(values[i:j+1])  # First half score 
                shs = self.minScoreTriangulation(values[j:] + values[:i+1])  # Second half score
                mts = min(mts, fhs + shs)
                
        return mts

# Solution 2 
class Solution:
    def helper(self, values, mem):
        tvals = tuple(values)
        if tvals in mem:
            return mem[tvals]
        
        if len(values) < 3:
            # So that any invalid polygons are automatically left out.
            mem[tvals] = inf
            return mem[tvals] 
        
        if len(values) == 3:
            # We already know a triangle's miniumum triangualtion score.
            mem[tvals] = values[0]*values[1]*values[2]
            return mem[tvals]
        
        mts = inf  # Minimum triangulation score
        for i in range(len(values)-2):
            for j in range(i+2, len(values)):
                # i, j is the side we're picking in this iteration.
                
                # (0, N-1) can't be a side.
                if i == 0 and j == len(values)-1:
                    continue
                 
                fhs = self.minScoreTriangulation(values[i:j+1])  # First half score 
                shs = self.minScoreTriangulation(values[j:] + values[:i+1])  # Second half score
                mts = min(mts, fhs + shs)
         
        mem[tvals] = mts
        return mem[tvals]
    
    def minScoreTriangulation(self, values: List[int]) -> int:
        return self.helper(values, {})


# Solution 3 - From discuss
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        N = len(values)
        dp = [[0 for _ in range(N+1)] for __ in range(N+1)]
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j] if dp[i][j] != 0 else inf,
                                   dp[i][k] + values[i]*values[k]*values[j] + dp[k][j])
                 
        return dp[0][N-1]