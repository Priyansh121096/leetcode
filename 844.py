# https://leetcode.com/problems/backspace-string-compare/
# 844. Backspace String Compare

# Solution 1 - Stacks
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

# Solution 2 - no extra space
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        
        for i, c in enumerate(s):
            if c != '#':
                continue
                
            s[i] = None
            j = i-1
            while j >= 0 and s[j] is None:
                j -= 1
            if j >= 0:
                s[j] = None
        s = [c for c in s if c is not None]
        
        for i, c in enumerate(t):
            if c != '#':
                continue
                
            t[i] = None
            j = i-1
            while j >= 0 and t[j] is None:
                j -= 1
            if j >= 0:
                t[j] = None        
        t = [c for c in t if c is not None]
        
        return s == t


# Solutiuon 3 - start from back
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        while (i >= 0) or (j >= 0):
            cs, ct = (s[i] if i >= 0 else ''), (t[j] if j >= 0 else '')
            if '#' not in (cs, ct):
                if cs != ct:
                    return False
                
                i -= 1
                j -= 1
                continue
                
            if cs == '#':
                i -= 1
                hc, sc = 1, 0
                while i >= 0 and hc > sc:
                    if s[i] == '#':
                        hc += 1
                    else:
                        sc += 1
                    i -= 1
            
            if ct == '#':
                j -= 1
                hc, sc = 1, 0
                while j >= 0 and hc > sc:
                    if t[j] == '#':
                        hc += 1
                    else:
                        sc += 1
                    j -= 1
                
        
        return True
