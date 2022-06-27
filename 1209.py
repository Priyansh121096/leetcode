# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# 1209. Remove All Adjacent Duplicates in String II

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            elif stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        out = []
        for char, count in stack:
            out.extend([char]*count)
        
        return "".join(out)