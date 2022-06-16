# https://leetcode.com/problems/longest-palindromic-substring/
# 5. Longest Palindromic Substring

from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Odd length
        maxPal = [s[0]]
        for i in range(1, len(s)):
            pal = deque([s[i]])
            k = 1
            while i-k >= 0 and i+k < len(s) and s[i-k] == s[i+k]:
                pal.appendleft(s[i-k])
                pal.append(s[i+k])
                k += 1
            maxPal = max(maxPal, pal, key=len)
            
        # Even length
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                continue
                
            pal = deque([s[i], s[i+1]])
            k = 1
            while (i-k) >= 0 and (i+k+1) < len(s) and s[i-k] == s[i+k+1]:
                pal.appendleft(s[i-k])
                pal.append(s[i+k+1])
                k += 1

            maxPal = max(maxPal, pal, key=len)
            
        return "".join(maxPal)

# Shorter code
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        maxPal = [s[0]]
        for i in range(len(s)):
            maxPal = max(
                maxPal, 
                helper(i, i),   # Odd-length substrings
                helper(i, i+1), # Even-length substrings
                key=len,
            )
        
        return "".join(maxPal)

# A bit more optimized code
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def helper(i, j):
            while i >= 0 and j < N and s[i] == s[j]:
                i -= 1
                j += 1
            
            return (i+1, j-1)
        
        maxL = (0, 0)
        for i in range(N):
            odd = helper(i, i)
            even = helper(i, i+1)
            maxL = max([maxL, odd, even], key=lambda x: x[1]-x[0])
            
        return s[maxL[0]:maxL[1]+1]
