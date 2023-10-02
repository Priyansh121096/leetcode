# https://leetcode.com/problems/maximum-number-of-points-with-cost/
# 1937. Maximum Number of Points with Cost

# O(M*N*N) - TLE
class Solution:
    def maxPoints(self, pts: List[List[int]]) -> int:
        M, N = len(pts), len(pts[0])
        dp = pts[0]
        
        for i in range(1, M):
            new_dp = []
            for j in range(N):
                maxScore = -inf
                for k in range(N):
                    maxScore = max(dp[k] - abs(k - j), maxScore) 
                    
                new_dp.append(maxScore + pts[i][j])
                
            dp = new_dp
                
        return max(dp)


# O(M*N) - Accepted
class Solution:
    def maxPoints(self, pts: List[List[int]]) -> int:
        M, N = len(pts), len(pts[0])
        dp = pts[0]
        
        for i in range(1, M):
            left = [dp[0]]
            for j in range(1, N): left.append(max(left[-1]-1, dp[j]))
                
            right = [dp[-1]]
            for j in range(N-2, -1, -1): right.append(max(right[-1]-1, dp[j]))
            right = right[::-1]
            
            new_dp = []
            for j in range(N):
                new_dp.append(pts[i][j] + max(left[j], right[j]))
                
            dp = new_dp
                
        return max(dp)