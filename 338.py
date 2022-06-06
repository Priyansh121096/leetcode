# https://leetcode.com/problems/counting-bits/
# 338. Counting Bits

class Solution:
    def countBits(self, n: int) -> List[int]:    
        out = [0, 1, 1]  # out[i] is the number of 1 bits in `i`.
        lpo2 = 1  # The largest power of 2 we've received so far.
        for i in range(3, n+1):
            if i == (1 << (lpo2+1)):
                # If we receive the next power of 2, reset the count to 1
                # and increment lpo2.
                out.append(1)
                lpo2 += 1
            else:
                # out[i] = 1 + out[i - 2^lpo2]
                # e.g. 13 = 1101 == (1)(101) 
                # The first 1 bit is contributed by lpo2 (2^3) and the remaining part is 
                # 101=5; so out[13] = 1 + out[13-8]
                remove = 1 << lpo2
                rem_part = i - remove
                out.append(1 + out[rem_part])
                
        return out[:n+1] if n < 3 else out