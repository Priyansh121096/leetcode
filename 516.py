# https://leetcode.com/problems/longest-palindromic-subsequence/
# 516. Longest Palindromic Subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[1 for j in range(N)] for i in range(N)]
        maxPal = 1

        for k in range(1, len(s)):
            for i in range(len(s)-k):
                j = i+k
                if s[i] == s[j]:
                    dp[i][j] = max(
                        2 + (dp[i+1][j-1] if j > i + 1 else 0),
                        dp[i][j-1],
                        dp[i+1][j],
                    )
                else:
                    dp[i][j] = max(
                        dp[i][j-1],
                        dp[i+1][j],
                    )
                maxPal = max(maxPal, dp[i][j])
                    
        return maxPal