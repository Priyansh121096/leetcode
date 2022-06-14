# https://leetcode.com/problems/triangle/
# 120. Triangle
# https://leetcode.com/problems/triangle/discuss/2146464/Python-Two-DP-approaches

from functools import lru_cache

class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        @lru_cache
        def helper(i, j):
            if i == len(t)-1:
                return t[i][j]
            
            return t[i][j] + min(helper(i+1, j), helper(i+1, j+1))
                              
        return helper(0, 0)

# O(n) space
class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        dp = [inf for _ in range(len(t))]
        
        dp[0] = t[0][0]
        for i in range(1, len(t)):
            for j in range(i, -1, -1):
                if j == 0:
                    dp[j] += t[i][j]
                else:
                    dp[j] = t[i][j] + min(dp[j-1], dp[j])
                    
        return min(dp)