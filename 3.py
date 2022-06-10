# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# 3. Longest Substring Without Repeating Characters

# Sliding window + Hashset
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left, mlen = 0, 1
        chars = set(s[0])
        
        for i in range(1, len(s)):
            if s[i] in chars:
                while True:
                    chars.remove(s[left])
                    if s[i] == s[left]:
                        break
                    left += 1
                left += 1
       
            chars.add(s[i])
            clen = i-left+1
            mlen = max(mlen, clen)
            
        return mlen
   