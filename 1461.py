# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
# 1461. Check If a String Contains All Binary Codes of Size K

# Solution 1 (AC)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        isThere = [False]*(1<<k)
        i, j = 0, k-1
        while j < len(s):
            x = int(s[i:j+1], 2)
            #print(i, j, x)
            isThere[x] = True
            i += 1
            j += 1
           
        #print(isThere)
        return all(x is True for x in isThere)