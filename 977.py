# https://leetcode.com/problems/squares-of-a-sorted-array/
# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        while i < len(nums) and nums[i] < 0:
            i += 1
        
        j = i-1
        out = []
        while j >= 0 and i < len(nums):
            if nums[i] <= abs(nums[j]):
                out.append(nums[i]**2)
                i += 1
            else:
                out.append(nums[j]**2)
                j -= 1
                
        while j >= 0:
            out.append(nums[j]**2)
            j -= 1
            
        while i < len(nums):
            out.append(nums[i]**2)
            i += 1
            
        return out