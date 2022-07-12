# https://leetcode.com/problems/max-consecutive-ones-iii/
# 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        currLen = 1 if k > 0 or nums[0] == 1 else 0
        maxLen = currLen
        currK = k if nums[0] == 1 else max(-1, k-1)
        for i in range(1, len(nums)):
            if nums[i] == 0:
                currK -= 1
                
            while currK < 0 and left <= i:
                if nums[left] == 0:
                    currK += 1

                left += 1
                
            maxLen = max(maxLen, i-left+1)
            
        return maxLen
