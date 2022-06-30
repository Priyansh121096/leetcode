# https://leetcode.com/problems/valid-word-abbreviation/
# 408. Valid Word Abbreviation

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # print('=-===')
        currNum = []
        j = 0
        for a in abbr:
            if j >= len(word):
                return False
            # print(a, currNum, j, word[j])
            if a.isdigit():
                currNum.append(a)
                continue
            
            if not currNum:
                if word[j] != a:
                    return False
                j += 1
                continue
            
            if currNum[0] == '0':
                return False
            
            l = int("".join(currNum))
            currNum = []
            j += l
            if j >= len(word):
                return False
            
            if word[j] != a:
                return False
            j += 1
          
            
        if currNum:
            if currNum[0] == '0':
                return False
            l = int("".join(currNum))
            currNum = []
            j += l
        
        # print(currNum, j, len(word))
        return j == len(word) and currNum == []
            
            
            
                