# https://leetcode.com/problems/interleaving-string/
# 97. Interleaving String

# Top down DP (memoization)
from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N, C = map(len, (s1, s2, s3))
        
        if M + N != C:
            return False
        
        @lru_cache
        def dp(i, j):
            if i == M and j == N:
                return True
            
            match = False
            if i < M and s1[i] == s3[i+j]:
                match = dp(i+1, j)
                if match:
                    return True
            if j < N and s2[j] == s3[i+j]:
                match = dp(i, j+1)
                if match:
                    return True
                
            return False
        
        return dp(0, 0)
                

# Bottom-up DP
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N, C = map(len, (s1, s2, s3))
        
        if M + N != C:
            return False
        
        dp = [[False for j in range(N+1)] for i in range(M+1)]
        for i in range(M+1):
            for j in range(N+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
                    
        return dp[M][N]


# Bottom-up DP - space optimized
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N, C = map(len, (s1, s2, s3))
        
        if M + N != C:
            return False
        
        dp = [False for j in range(N+1)]
        for i in range(M+1):
            for j in range(N+1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] == s3[i+j-1])
                    
        return dp[N]
