# https://leetcode.com/problems/first-missing-positive

# O(n) + O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            while True:
                if not 0 < nums[i] < len(nums)+1:
                    break
                if nums[i] == i+1:
                    break
                if nums[nums[i] - 1] == nums[i]:
                    break
                
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        minNotFound = 1
        for x in nums:
            if x != minNotFound:
                break
            minNotFound += 1

        return minNotFound

# O(n) + O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minNotFound = 1
        nums = set(nums)
        while nums:
            x = nums.pop()
            if x <= 0:
                continue 

            if x <= minNotFound:
                minNotFound += 1
            
            while x+1 in nums:
                x += 1 
                nums.discard(x)
                if x <= minNotFound:
                    minNotFound += 1    

        return minNotFound            
