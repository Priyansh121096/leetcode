# https://leetcode.com/problems/find-pivot-index/
# 724. Find Pivot Index

# Three loops
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        
        leftSum = [0]
        for i in range(1, N):
            leftSum.append(leftSum[-1] + nums[i-1])
            
        rightSum = [0]
        for i in range(N-2, -1, -1):
            rightSum.append(rightSum[-1] + nums[i+1])
            
        for i in range(N):
            if leftSum[i] == rightSum[N-i-1]:
                return i
            
        return -1


# Two loops
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        
        leftSum = [0]
        rightSum = [0]
        for i in range(N):
            if i > 0:
                leftSum.append(leftSum[-1] + nums[i-1])
            if i < N-1:
                rightSum.append(rightSum[-1] + nums[N-i-1])
            
        for i in range(N):
            if leftSum[i] == rightSum[N-i-1]:
                return i
            
        return -1


# One loop
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        
        lSum, rSum = 0, sum(nums[1:])
        if lSum == rSum:
            return 0
        
        for i in range(1, N):
            lSum += nums[i-1]
            rSum -= nums[i]
            
            if lSum == rSum:
                return i
            
        return -1
