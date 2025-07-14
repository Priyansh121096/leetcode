# https://leetcode.com/problems/remove-invalid-parentheses/
class Solution:
    def helper(self, s, i, open_count, close, expr, out) -> None:
        if i == len(s):
            # Invalid string
            if open_count != close:
                return

            # Optimization to not include smaller strings as maxSoFar grows
            if len(expr) < self.maxSoFar:
                return
            self.maxSoFar = len(expr)

            out.add(''.join(expr))
            return

        char = s[i]

        if char not in ('(', ')'):
            # Regular character, simply include
            expr.append(char)
            self.helper(s, i+1, open_count, close, expr, out)
            expr.pop()
        elif char == ')' and open_count == close:
            # Redundant closing bracket; simply discard
            self.helper(s, i+1, open_count, close, expr, out)
        else:
            # Here we have a choice
            # A. Include this character
            expr.append(char)
            if char == '(':
                self.helper(s, i+1, open_count+1, close, expr, out)
            else:
                self.helper(s, i+1, open_count, close+1, expr, out)
            expr.pop()

            # A. Do not include this character
            self.helper(s, i+1, open_count, close, expr, out)

    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.maxSoFar = 0
        out = set()
        self.helper(s, 0, 0, 0, [], out)
        return [expr for expr in out if len(expr) == self.maxSoFar]
