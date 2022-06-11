# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# 1658. Minimum Operations to Reduce X to Zero


# Prefix+suffix sum + two sum using binary search - O(nlogn) time and O(n) space.
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # If x is less than the extemeties; we can never reduce it to 0.
        if x < nums[0] and x < nums[-1]:
            return -1
        
        # If x is equal to one of the extemeties; we only need one operation.
        if x in (nums[0], nums[-1]):
            return 1
        
        # Calculate the prefix sum of nums and also see if 
        # it includes x itself in which case note down the 
        # number of operations it takes to reach x (minL).
        minL, lsum = inf, [nums[0]]
        for i in range(1, len(nums)):
            cSum = lsum[-1] + nums[i]
            if minL is inf and cSum == x:
                minL = i+1
            lsum.append(cSum)
            
        # Calculate the suffix sum of nums and also see if 
        # it includes x itself in which case note down the 
        # number of operations it takes to reach x (minR).
        # Note that we're not reversing the rsum array as we
        # usually do. 
        minR, rsum = inf, [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            cSum = rsum[-1] + nums[i]
            if minR is inf and cSum == x:
                minR = len(nums)-i
            rsum.append(cSum)
            
        # For each element in the prefix sum, search for a corresponding
        # element in the suffix sum such that it sums up to x. Note that,
        # to prevent double counting, we must finish our search in the rsum
        # array before the ith element of lsum.
        minBoth = inf
        for i in range(len(lsum)-1):
            lnum = lsum[i]
            tgt = x - lnum
            
            # Binary search
            l, r = 0, len(rsum)-i-2
            while l <= r:
                m = l + (r-l) // 2
                if rsum[m] == tgt:
                    minBoth = min(minBoth, i+m+2)
                    break
                elif rsum[m] > tgt:
                    r = m-1
                else:
                    l = m+1
    
        return ans if (ans:=min(minL, minR, minBoth)) is not inf else -1


# Prefix+suffix sum + two sum using hashmap - O(n) time and O(n) space.
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # If x is less than the extemeties; we can never reduce it to 0.
        if x < nums[0] and x < nums[-1]:
            return -1
        
        # If x is equal to one of the extemeties; we only need one operation.
        if x in (nums[0], nums[-1]):
            return 1
        
        # Calculate the prefix sum of nums and also see if 
        # it includes x itself in which case note down the 
        # number of operations it takes to reach x (minL).
        minL, lsum = inf, [nums[0]]
        for i in range(1, len(nums)):
            cSum = lsum[-1] + nums[i]
            if minL is inf and cSum == x:
                minL = i+1
            lsum.append(cSum)
            
        # Calculate the suffix sum of nums and also see if 
        # it includes x itself in which case note down the 
        # number of operations it takes to reach x (minR).
        # Note that we're not reversing the rsum array as we
        # usually do. 
        minR, rsum = inf, [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            cSum = rsum[-1] + nums[i]
            if minR is inf and cSum == x:
                minR = len(nums)-i
            rsum.append(cSum)
         
        # Reduce to a two sum problem with 2 different arrays
        # i.e. find x-lsum[i] in rsum.
        minBoth = inf
        d = {x-lsum[i]: i for i in range(len(lsum)-1)}
        for j in range(len(rsum)-1):
            if rsum[j] in d and (i:=d[rsum[j]]) < len(rsum)-1-j:
                minBoth = min(minBoth, i+j+2)
    
        return ans if (ans:=min(minL, minR, minBoth)) is not inf else -1

# Largest subarray summing up to total - x; sliding window
# O(n) time and O(1) space
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # If x is less than the extemeties; we can never reduce it to 0.
        if x < nums[0] and x < nums[-1]:
            return -1
        
        # If x is equal to one of the extemeties; we only need one operation.
        if x in (nums[0], nums[-1]):
            return 1
        
        # Sliding window approach to find the longest subarray with 
        # sum == total - x
        tgt = sum(nums) - x
        left, currSum = 0, nums[0]
        maxLen = -inf if currSum != tgt else 1
        for right in range(1, len(nums)):
            currSum += nums[right]
            
            while left <= right and currSum > tgt:
                currSum -= nums[left]
                left += 1
                
            if currSum == tgt:
                maxLen = max(maxLen, right-left+1)
        
        return (len(nums) - maxLen) if maxLen != -inf else -1
