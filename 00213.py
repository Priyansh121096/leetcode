# https://leetcode.com/problems/house-robber-ii/
# 213. House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev, curr = 0, nums[0]
        for i in range(1, len(nums)-1):
            nxt = max(nums[i] + prev, curr)
            prev = curr
            curr = nxt
        currA = curr
        
        prev, curr = 0, nums[1]
        for i in range(2, len(nums)):
            nxt = max(nums[i] + prev, curr)
            prev = curr
            curr = nxt
        currB = curr
        
        return max(currA, currB)
        

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prevA, currA = 0, nums[0]
        prevB, currB = 0, nums[1]
        for i in range(1, len(nums)):
            if i != len(nums)-1:
                nxtA = max(nums[i] + prevA, currA)
                prevA = currA
                currA = nxtA
            if i != 1:
                nxtB = max(nums[i] + prevB, currB)
                prevB = currB
                currB = nxtB
        
        return max(currA, currB)
        
        