# https://leetcode.com/problems/3sum/
# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        
        if N < 3:
            return []
        
        nums = sorted(nums)
        print(nums)
        out = []
        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, N-1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0:
                    out.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                        
                elif currSum > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif currSum < 0:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
        return out
                    
        
        