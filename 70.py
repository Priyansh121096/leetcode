# https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
         
        prev, prevprev = 2, 1
        for i in range(2, n):
            old_prev = prev
            prev += prevprev
            prevprev = old_prev
            
        return prev
        