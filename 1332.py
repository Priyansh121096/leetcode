# https://leetcode.com/problems/remove-palindromic-subsequences/
# 1332. Remove Palindromic Subsequences

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """
        If the string is empty; we can remove all palindromes in 0 steps.
        If the string is a palindrome; we can remove all palindromes in 1 step.
        Else, we can remove all 'a's once and all 'b's once to make the string
        empty. This is because we need to remove subsequences (not substrings)
        and strings containing all 'a's and all 'b's are palindromes.
        """
        N = len(s)
        
        if N % 2 == 0:
            left, right = N//2 - 1, N//2
        else:
            left, right = N//2 - 1, N//2 + 1
            
        try:
            while s[left] == s[right]:
                left -= 1
                right += 1
        except IndexError:
            return 1

        return 2
