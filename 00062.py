# https://leetcode.com/problems/unique-paths/
# 62. Unique Paths

# DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
                
        return dp[-1]

# Math
from math import factorial as f

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        
        return f(m+n-2) // f(m-1) // f(n-1)

# Math with simplification
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        
        # If it's a MxN grid, you have to make M-1 "down turns" and N-1 "right" turns.
        m -= 1
        n -= 1
        
        # ans = (m+n)! // (m!*n!)
        # ans = (1.2.3.4...m.m+1.m+2...m+n) // (1.2.3.4...m) * (1.2.3.4...n)
        # ans = (m+1.m+2...m+n) // (1.2.3.4...n)
        
        # Keep m bigger because it gets nullified in the above formula.
        if n > m:
            m, n = n, m
        
        # Calculate (m+1.m+2...m+n) // (1.2.3.4...n)
        ans = 1
        for i in range(m+1, m+n+1):
            ans *= i
            ans /= (i-m)
        
        return int(ans)