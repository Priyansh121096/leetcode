# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number

class Solution:
    D = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    
    def helper(self, comb, i):
        if i == self.N:
            self.out.append("".join(comb[:]))
            return
        
        for char in self.D[self.dits[i]]:
            comb.append(char)
            self.helper(comb, i+1)
            comb.pop()
    
    def letterCombinations(self, digits: str) -> List[str]:
        self.out = []
        self.dits = digits
        self.N = len(digits)
        
        if self.N == 0:
            return []
        
        for char in self.D[digits[0]]:
            self.helper([char], 1)
        
        return self.out