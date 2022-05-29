# https://leetcode.com/problems/maximum-product-of-word-lengths/
# 318. Maximum Product of Word Lengths

# Thought of sorting, hashmap, tries, DP.
# Saw idea of bit representations from Discuss titles.

# Solution 1 (AC)
# TC: O(n^2); SC: O(n)
class Solution:
    def getBin(self, word):
        arr = ['0']*26
        for w in word:
            arr[ord(w) - ord('a')] = '1'
            
        return int(''.join(arr), 2)
    
    def maxProduct(self, words) -> int:
        bins = [self.getBin(w) for w in words]
        
        mprod = float('-inf')
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if bins[i] & bins[j] == 0:
                    mprod = max(mprod, len(words[i])*len(words[j]))
                    
        return mprod if mprod != float('-inf') else 0