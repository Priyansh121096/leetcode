# https://leetcode.com/problems/delete-operation-for-two-strings/
# 583. Delete Operation for Two Strings

# O(MN) time and O(MN) space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[inf for _ in range(N+1)] for __ in range(M+1)]
        
        for i in range(M+1):
            for j in range(N+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] != word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = min(
                        1 + min(dp[i-1][j], dp[i][j-1]),
                        dp[i-1][j-1],
                    )
         
        return dp[M][N]
                    

# Space optimized DP - O(MN) time and O(N) space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [j for j in range(N+1)]
        
        for i in range(1, M+1):
            new_dp = []
            for j in range(N+1):
                if j == 0:
                    elem = i
                elif word1[i-1] != word2[j-1]:
                    elem = 1 + min(dp[j], new_dp[j-1])
                else:
                    elem = min(1 + min(dp[j], new_dp[j-1]), dp[j-1])
                
                new_dp.append(elem)

            dp = new_dp
         
        return dp[-1]

# One more optimization - O(MN) time and O(min(M, N)) space
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        
        M, N = len(word1), len(word2)
        dp = [j for j in range(N+1)]
        
        for i in range(1, M+1):
            new_dp = []
            for j in range(N+1):
                if j == 0:
                    elem = i
                elif word1[i-1] != word2[j-1]:
                    elem = 1 + min(dp[j], new_dp[j-1])
                else:
                    elem = min(1 + min(dp[j], new_dp[j-1]), dp[j-1])
                
                new_dp.append(elem)

            dp = new_dp
         
        return dp[-1]
