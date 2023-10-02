# https://leetcode.com/problems/coin-change/
# 322. Coin Change

class Solution:
    def coinChange(self, c: List[int], amt: int) -> int:
        dp = [[inf for _ in range(amt+1)] for __ in range(len(c))]
        
        for i in range(len(c)):
            for j in range(amt+1):
                if j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = inf if (j % c[i] != 0) else (j // c[i])
                else:
                    if c[i] > j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = min(1+dp[i][j-c[i]], dp[i-1][j])
             
        #print(dp)
        return dp[len(c)-1][amt] if dp[len(c)-1][amt] != inf else -1
                

#  Space optimized DP
class Solution:
    def coinChange(self, c: List[int], amt: int) -> int:
        dp = [inf for _ in range(amt+1)]
        
        for i in range(len(c)):
            for j in range(amt+1):
                if j == 0:
                    dp[j] = 0
                elif i == 0:
                    dp[j] = inf if (j % c[i] != 0) else (j // c[i])
                elif c[i] <= j:
                    dp[j] = min(1+dp[j-c[i]], dp[j])

        return dp[amt] if dp[amt] != inf else -1
                    