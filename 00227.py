# https://leetcode.com/problems/basic-calculator-ii

class Solution:
    def calculate(self, s: str) -> int:
        num, op = None, None
        stack = []
        ops = ['/', '*', '-', '+']
        for c in s:
            if c == ' ':
                continue
            elif c in ops:
                if op:
                    stack.append((num, op))
                else:
                    stack.append((num, None))
                op = c
                num = None
            else:
                if num is None:
                    num = int(c)
                else:
                    num = num*10 + int(c)
        stack.append((num, op))
        
        nstack = []
        for num, op in stack:
            if op not in ('/', '*'):
                nstack.append((num, op))
            else:
                x, pop = nstack.pop()
                if op == '/':
                    nstack.append((x // num, pop))
                else:
                    nstack.append((x * num, pop))
        stack = nstack

        nstack = []
        for num, op in stack:
            if op not in ('-', '+'):
                nstack.append((num, op))
            else:
                x, pop = nstack.pop()
                if op == '-':
                    nstack.append((x - num, pop))
                else:
                    nstack.append((x + num, pop))
        stack = nstack

        return stack[0][0]
                
