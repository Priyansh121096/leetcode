# https://leetcode.com/problems/consecutive-characters/
# 1446. Consecutive Characters

class Solution:
    def maxPower(self, s: str) -> int:
        clen, mlen = 1, 1
        char = s[0]
        for i in range(1, len(s)):
            if s[i] == char:
                clen += 1
            else:
                mlen = max(mlen, clen)
                clen = 1
                char = s[i]
                
        return max(mlen, clen)