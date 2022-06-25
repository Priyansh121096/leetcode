# https://leetcode.com/problems/3sum-closest/
# 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N == 3:
            return sum(nums)
        
        nums = sorted(nums)
        minSum, minDiff = None, float("inf")
        
        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, N-1
            
            while left < right:
                currSum = sum([nums[i], nums[left], nums[right]])
                currDiff = abs(target - currSum)

                if currDiff < minDiff:
                    minDiff = currDiff
                    minSum = currSum

                    if minDiff == 0:
                        return minSum

                if target > currSum:
                    left += 1
                    while left < N and nums[left] == nums[left-1]:
                        left += 1
                else:
                    right -= 1
                    while right >= 0 and nums[right] == nums[right+1]:
                        right -= 1
        
        return minSum