# https://leetcode.com/problems/non-decreasing-array/
# 665. Non-decreasing Array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)
        error = False
        
        i = 0
        while i < N-1:
            # This pair is already non-decreasing (ND)l do nothing
            if nums[i] <= nums[i+1]:
                i += 1
                continue
                
            # This pair is not ND...
                
            # If a modification has already happened before; no further 
            # modifications can be done.
            if error:
                return False
            
            # If no error has occurred so far and we're at the second last
            # element; the last element can be modified to make it ND.
            if i == N-2:
                return True
            
            # The below two conditionals check if either of i and i+1 can be
            # set to the other to satisfy nums[i-1] <= nums[i] <= nums[i+1].
            
            # Can nums[i] be set to nums[i+1]?
            if (i == 0 or nums[i+1] >= nums[i-1]) and nums[i+1] <= nums[i+2]:
                error = True
                i += 2
                continue
                
            # Can nums[i+1] be set to nums[i]?
            if nums[i] <= nums[i+2]:
                error = True
                i += 2
                continue

            # If we've reached here; no modification is possible for this pair
            # to make it ND.
            return False
            
        return True
