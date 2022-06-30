# https://leetcode.com/problems/queue-reconstruction-by-height/
# 406. Queue Reconstruction by Height

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        N = len(people)
        people = sorted(people, key=lambda hk: hk[0]* (10**6) + hk[1])
        
        arr = [None]*N
        for (h, k) in people:
            s = 0
            i = 0
            while s < k:
                if arr[i] is None or arr[i][0] == h:
                    s += 1
                    
                i += 1
            
            while arr[i] is not None:
                i += 1
                
            arr[i] = [h, k]
            
        return arr


# Simple
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda hk: (-hk[0], hk[1]))
        
        output = []
        for h, k in people:
            output.insert(k, [h, k])
        
        return output