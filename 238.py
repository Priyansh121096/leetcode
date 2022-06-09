# https://leetcode.com/problems/product-of-array-except-self/
# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums[::-1]
        
        pp = [nums[0]]
        for i in range(1, len(nums)):
            pp.append(pp[-1]*nums[i])
            
        sp = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            sp.append(sp[-1]*nums[i])
        sp = sp[::-1]
        
        #print(pp, sp)
        
        out = [sp[1]]
        for i in range(1, len(nums)-1):
            out.append(pp[i-1]*sp[i+1])
        out.append(pp[-2])
            
        return out
            

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre               # prefix product from one end
            pre *= nums[i]
            ans[-1-i] *= suf            # suffix product from other end
            suf *= nums[-1-i]
        return ans

        
        