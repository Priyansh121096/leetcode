# https://leetcode.com/problems/best-sightseeing-pair/
# 1014. Best Sightseeing Pair

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # maximise A[i] + i + A[j] - j
        left = values[0] + 0  # Best A[i] + i we've found so far
        maxValue = 0
        for i in range(1, len(values)):
            # Update maxValue with the current A[i] - i (right) and the 
            # best A[i] + i we've found so far (left)
            maxValue = max(maxValue, left + values[i] - i)
            # If this is a better left (A[i] + i), update left. 
            left = max(left, values[i] + i)
            
        return maxValue