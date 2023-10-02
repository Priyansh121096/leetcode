# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, t: List[str]) -> int:
        N = len(t)
        stack = []
        for i in range(N):
            char = t[i]
            if char in ("/", "+", "-", "*"):
                b, a = stack.pop(), stack.pop()
                
                if char == '/':
                    c = int(a / b)
                elif char == '*':
                    c = a * b
                elif char == '+':
                    c = a + b
                else:
                    c = a - b
                
                stack.append(c)
            else:
                stack.append(int(char))
                
        return stack.pop()