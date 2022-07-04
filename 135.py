# https://leetcode.com/problems/candy/
# 135. Candy

class Solution:
    def candy(self, rats: List[int]) -> int:
        N = len(rats)
        if N == 1:
            return 1
        
        out = [1]*N
        
        # Left to right
        for i in range(1, N):
            if rats[i] > rats[i-1]:
                out[i] = 1 + out[i-1]
                
        # Right to left
        for i in range(N-2, -1, -1):
            if rats[i] > rats[i+1]:
                out[i] = max(out[i], 1+out[i+1])
        
        return sum(out)
        