# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# 698. Partition to K Equal Sum Subsets

# Brute-force backtracking (TLE)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        
        def helper(i, subs):
            if i == N:
                return all(x == subs[0] for x in subs)
            
            for j in range(k):
                subs[j] += nums[i]
                if helper(i+1, subs) is True:
                    return True
                subs[j] -= nums[i]
                
            return False
        
        return helper(0, [0]*k)


# Better (sort in desc order so that invalid candidates are invalidated early) - still TLE
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        S = sum(nums)
        
        # Figure out the sum each subset must sum up to.
        if S % k != 0:
            return False
        A = S // k
        
        nums = sorted(nums, reverse=True)
        subs = [0]*k
        
        def helper(i):
            if i == N:
                return True
            
            for j in range(k):
                subs[j] += nums[i]
                if subs[j] <= A and helper(i+1) is True:
                    return True
                subs[j] -= nums[i]
                
            return False
        
        return helper(0)