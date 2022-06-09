# https://leetcode.com/problems/backspace-string-compare/
# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        for i in range(len(s)):
            if s[i] != '#':
                s1.append(s[i])
            elif s1:
                s1.pop()
                
        s2 = []
        for i in range(len(t)):
            if t[i] != '#':
                s2.append(t[i])
            elif s2:
                s2.pop()
                
        return s1 == s2
