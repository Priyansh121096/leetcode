# https://leetcode.com/problems/generalized-abbreviation/
# 320. Generalized Abbreviation
# Solution: https://leetcode.com/problems/generalized-abbreviation/discuss/2221373/Python-Bitmasking

class Solution:
    def getAbbrForBitMask(self, word:str, bitmask: int) -> str:
        bitmask = format(bitmask, f"0{len(word)}b")
        out = []
        currStreak = 0
        for i in range(len(word)):
            if bitmask[i] == "0":
                currStreak += 1
            else:
                if currStreak:
                    out.append(str(currStreak))
                    currStreak = 0
                
                out.append(word[i])
               
        if currStreak:
            out.append(str(currStreak))
            
        return "".join(out)
    
    def generateAbbreviations(self, word: str) -> List[str]:
        N = len(word)
        
        out = []
        for bitmask in range(2**N):
            out.append(self.getAbbrForBitMask(word, bitmask))
        
        return out