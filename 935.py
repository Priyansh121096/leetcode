# https://leetcode.com/problems/knight-dialer/
# 935. Knight Dialer

class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9+7
        moves = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
        }
        
        counts = [1]*10
        for i in range(n-1):
            next_counts = [0]*10
            for src in range(10):
                for dest in moves[src]:
                    next_counts[dest] = (next_counts[dest] + counts[src]) % mod
                    
            counts = next_counts
            
        return sum(counts) % mod