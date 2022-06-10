# https://leetcode.com/problems/permutations/
# 46. Permutations

class Solution:
    def helper(self, rem, perm):
        if not rem:
            self.out.append(perm[:])
            return
        
        for num in rem:
            perm.append(num)
            nrem = rem - {num}
            self.helper(nrem, perm)
            perm.pop()
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.out = []
        
        for num in nums:
            rem = set(nums) - {num}
            self.helper(rem, [num])
            
        return self.out


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return nums and [
            p[:i] + [nums[0]] + p[i:]
            for p in self.permute(nums[1:])
            for i in range(len(nums))
        ] or [[]]