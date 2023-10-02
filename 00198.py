# https://leetcode.com/problems/house-robber/
# 198. House Robber

class Solution:
    def rob(self, n: List[int]) -> int:
        dp = [0, n[0]]
        for i in range(1, len(n)):
            dp.append(max(n[i] + dp[i-1], dp[i]))
        return dp[-1]

# Constant space
class Solution:
    def rob(self, n: List[int]) -> int:
        prev, curr = 0, n[0]
        for i in range(1, len(n)):
            nxt = max(prev + n[i], curr)
            prev = curr
            curr = nxt
        
        return curr