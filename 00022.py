# https://leetcode.com/problems/generate-parentheses/
# 22. Generate Parentheses

class Solution:
    def helper(self, comb, op, cl):
        # If there are no more open brackets,
        # attach the remaining closing brackets,
        # append to the output array and return.
        if op == self.n:
            ans = comb + [')']*(op-cl)
            self.out.append("".join(ans))
            return
        
        # If #closing brackets > #opening brackets,
        # it's an invalid combination.
        if cl > op:
            return
        
        comb.append('(')
        self.helper(comb, op+1, cl)
        comb[-1] = ')'
        self.helper(comb, op, cl+1)
        comb.pop()
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.out = []
        self.n = n
        # All parentheses start with exactly one open bracket.
        self.helper(['('], 1, 0)
        return self.out


# Python generators
class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield "".join(p)
                else:
                    p.append('(')
                    yield from generate(p, left-1, right)
                    p[-1] = ')'
                    yield from generate(p, left, right-1)
                    p.pop()
        
        return list(generate([], n, n))