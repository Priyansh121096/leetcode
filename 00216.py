# https://leetcode.com/problems/combination-sum-iii/
# 216. Combination Sum III

class Solution:
    def helper(self, comb, remSum, i):
        if remSum < 0:
            return 
        
        if len(comb) > self.k:
            return
        
        if remSum == 0 and len(comb) == self.k:
            self.out.append(comb[:])
        
        # Note that we only recurse from i+1 onward.
		# This helps make sure, there are not duplicate combinations.
		# This is different from permutations where we iterate over 
		# every remaining element and not just the ones after.
        for num in range(i+1, 10):
            comb.append(num)
            self.helper(comb, remSum - num, num)
            comb.pop()
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.out = []
        self.k = k
        
        for num in range(1, 10):
            self.helper([num], n-num, num)
            
        return self.out