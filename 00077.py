# https://leetcode.com/problems/combinations/
# 77. Combinations

# Reduce it to finding subsets problem - find subsets of length k
class Solution:
    @staticmethod
    def getComb(n, bitmask, k):
        comb = []
        for i in range(1, n+1):
            bit = bitmask & 1
            if bit:
                comb.append(i)
            if len(comb) > k:
                return 
            bitmask >>= 1
            
        if len(comb) == k:
            return comb
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [comb for bitmask in range(2**n) 
                if (comb:= self.getComb(n, bitmask, k)) is not None]


# Optimal backtracking
class Solution:    
    def helper(self, comb, i, n, k):
        if k == 0:
            self.out.append(comb[:])
            return
        
        for j in range(i+1, n+1):
            comb.append(j)
            self.helper(comb, j, n, k-1)
            comb.pop()
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.out = []
        for i in range(1, n+1):
            self.helper([i], i, n, k-1)
        
        return self.out