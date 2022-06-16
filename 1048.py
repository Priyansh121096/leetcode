# https://leetcode.com/problems/longest-string-chain/
# 1048. Longest String Chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        N = len(words)
        dp = [1]*N
        
        def isPredecessor(pred, suc):
            if len(pred) != (len(suc) + 1):
                return False
            
            error = False
            for i in range(len(pred)):
                if error and pred[i] != suc[i-1]:
                    return False
                elif not error and (i == len(suc) or pred[i] != suc[i]):
                    error = True
                    
            return True
            
        for i in range(1, N):
            for j in range(i-1, -1, -1):
                if (1 + dp[j] > dp[i]) and isPredecessor(words[i], words[j]):
                    dp[i] = 1 + dp[j]
                    
        return max(dp)
                