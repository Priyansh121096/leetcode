# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -1 * abs(nums[abs(nums[i])-1])
            
        return [i+1 for i, x in enumerate(nums) if x > 0]