# https://leetcode.com/problems/subarray-sum-equals-k/
# 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        currSum = 0
        count = 0
        for num in nums:
            currSum += num
            
            if currSum - k in d:
                count += d[currSum-k]
                
            if currSum not in d:
                d[currSum] = 1
            else:
                d[currSum] += 1
            
        return count
