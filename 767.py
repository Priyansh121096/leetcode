# https://leetcode.com/problems/reorganize-string/
# 767. Reorganize String

# Heap based solution
from collections import Counter
from heapq import heapify, heappush, heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        out, temp = [], None
        
        # Create a max heap of the counts
        heap = [(-count, char) for char, count in c.items()]
        heapify(heap)
        
        for i in range(len(s)):
            # If there's no character in the heap and we're still in the loop;
            # this string cannot be converted.
            if not heap:
                return ""
            
            # Remove the most frequent character from the heap.
            temp2 = heappop(heap)
            
            # If the max freq is 0; there are no characters left but 
            # since we're still in the loop, this means that this string
            # cannot be converted.
            if temp2[0] == 0:
                return ""
            
            # Append the most frequent character to the output.
            out.append(temp2[1])
            
            # Next time the count will be 1 less but since we're storing the 
            # negatives of counts (to simulate a max heap), add 1 to the count.
            temp2 = (temp2[0]+1, temp2[1])
            
            # If there's an element left from the last time; push it to the heap
            if temp: heappush(heap, temp)
                
            # Next time, temp2 will be pushed to the heap
            temp = temp2 if temp2[0] < 0 else None
        
        return "".join(out)


# O(n) time - counting
class Solution:
    def reorganizeString(self, s: str) -> str:
        N = len(s)
        
        bkts = [0 for _ in range(26)]
        mf, mc = -inf, None
        for char in s:
            idx = ord(char)-ord('a')
            bkts[idx] += 1
            if bkts[idx] > mf:
                mf = bkts[idx]
                mc = char
                
            if (N % 2 == 0 and mf > N//2) or (N % 2 != 0 and mf > (N//2 + 1)):
                return ""
        
        out = [None for _ in range(N)]
        even, odd = 0, 1
        
        for i in range(mf):
            out[even] = mc
            even += 2
        bkts[ord(mc) - ord('a')] = 0
        
        for i in range(26):
            if bkts[i] == 0:
                continue
            char = chr(i+ord('a'))
            
            while bkts[i] > 0 and even < N:
                out[even] = char
                bkts[i] -= 1
                even += 2
                
            while bkts[i] > 0 and odd < N:
                out[odd] = char
                bkts[i] -= 1
                odd += 2
                
        return "".join(out)
        