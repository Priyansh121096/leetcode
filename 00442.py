# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# 442. Find All Duplicates in an Array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        for i, num in enumerate(nums):
            if nums[abs(num)-1] < 0:
                dups.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
                
        return dups