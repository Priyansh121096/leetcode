# https://leetcode.com/problems/contains-duplicate/
# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev == nums[i]:
                return True
            prev = nums[i]
        
        return False
        