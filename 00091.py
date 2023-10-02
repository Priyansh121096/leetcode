# https://leetcode.com/problems/decode-ways/
# 91. Decode Ways

# Recursion + Memoization
from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        
        @lru_cache
        def helper(i):
            if i == N:
                return 1
            
            ans = 0
            if s[i] != '0':
                ans += helper(i+1)
            if i+1 < N and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6)):
                ans += helper(i+2)
            
            return ans
        
        return helper(0)

# Bottom-up DP
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0 for _ in range(N)]
        
        for i in range(N-1, -1, -1):
            if i == N-1 and s[i] != '0':
                dp[i] = 1
                continue
            
            ans = 0
            if s[i] != '0':
                ans += dp[i+1]
            if i+1 < N and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6)):
                ans += dp[i+2] if i+2 < N else 1
            dp[i] = ans
        
        return dp[0]
