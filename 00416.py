# https://leetcode.com/problems/partition-equal-subset-sum/
# 416. Partition Equal Subset Sum

class Solution:
    def canPartition(self, n: List[int]) -> bool:
        s = sum(n)
        if s % 2 != 0:
            return False
        
        tgt = s // 2
        dp = [False for _ in range(tgt+1)]
        dp[0] = True
        for i in range(len(n)):
            for j in range(tgt, 0, -1):
                if n[i] <= j:
                    dp[j] |= dp[j-n[i]]
          
        return dp[tgt]
