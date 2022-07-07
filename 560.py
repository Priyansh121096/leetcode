# https://leetcode.com/problems/subarray-sum-equals-k/
# 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        cumSum = 0
        count = 0
        for num in nums:
            cumSum += num
            
            if cumSum - k in d:
                count += d[cumSum-k]
                
            d[cumSum] = d.get(cumSum, 0) + 1
            
        return count
