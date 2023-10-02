# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# 1423. Maximum Points You Can Obtain from Cards

# Intuition is similar to https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Find subarray of length N-K with the minimum sum

class Solution:
    def maxScore(self, cardPoints: List[int], K: int) -> int:
        N = len(cardPoints)
        J = N-K  # Minimum sum subarray of this length
        tSum = sum(cardPoints)
        cSum = sum(cardPoints[:J])
        mSum = cSum
        for i in range(1, N-J+1):
            cSum = cSum - cardPoints[i-1] + cardPoints[i+J-1]
            mSum = min(mSum, cSum)
            
        return tSum - mSum


# Compute tSum together
class Solution:
    def maxScore(self, cardPoints: List[int], K: int) -> int:
        N = len(cardPoints)
        J = N-K  # Minimum sum subarray of this length
        mSum = tSum = cSum = sum(cardPoints[:J])
        for i in range(1, N-J+1):
            tSum += cardPoints[i+J-1]
            cSum = cSum - cardPoints[i-1] + cardPoints[i+J-1]
            mSum = min(mSum, cSum)
            
        return tSum - mSum