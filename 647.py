# https://leetcode.com/problems/palindromic-substrings/
# 647. Palindromic Substrings

# Iteration + Recursion
class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        
        count = 0
        for i in range(len(s)):
            count += helper(i, i)
            count += helper(i, i+1)
            
        return count

# DP
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [[False for _ in range(N)] for __ in range(N)]
        count = 0
        for k in range(N):
            for i in range(N-k):
                j = i + k
                if i > j:
                    continue
                elif i == j:
                    dp[i][j] = True
                    count += 1
                elif s[i] == s[j]:
                    dp[i][j] = True if i == j-1 else dp[i+1][j-1]
                    count += 1 if dp[i][j] else 0
                    
        return count