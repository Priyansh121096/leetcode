# https://leetcode.com/problems/word-break/
# 139. Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [True]
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] in words and dp[j]:
                    dp.append(True)
                    break
            else:
                dp.append(False)
                
        return dp[-1]

# Don't look for substrings longer than the length of the 
# longest word in wordDict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [True]
        maxWordLen = len(max(words, key=len))
        for i in range(len(s)):
            start = max(0, i-maxWordLen+1)
            for j in range(start, i+1):
                if s[j:i+1] in words and dp[j]:
                    dp.append(True)
                    break
            else:
                dp.append(False)
                
        return dp[-1]