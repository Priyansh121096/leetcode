# https://leetcode.com/problems/permutations/
# 46. Permutations

class Solution:
    def helper(self, nums, perm):
        if self.N == len(perm):
            self.out.append(perm[:])
            return 
        
        for num in nums:
            perm.append(num)
            newSet = nums - {num}
            self.helper(newSet, perm)
            perm.pop()
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.N = len(nums)
        self.out = []
        self.helper(set(nums), [])
        return self.out


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return nums and [
            p[:i] + [nums[0]] + p[i:]
            for p in self.permute(nums[1:])
            for i in range(len(nums))
        ] or [[]]