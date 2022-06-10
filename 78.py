# https://leetcode.com/problems/subsets/
# 78. Subsets

class Solution:
    @staticmethod
    def getSubset(nums, bitmask):
        sub = []
        for i in range(len(nums)):
            bit = bitmask & 1
            if bit:
                sub.append(nums[i])
            bitmask >>= 1
        return sub
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [self.getSubset(nums, bitmask) for bitmask in range(1 << len(nums))]