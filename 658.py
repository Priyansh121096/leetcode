# https://leetcode.com/problems/find-k-closest-elements/
# 658. Find K Closest Elements

# Binary search suboptimal
class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums)
        
        if x <= nums[0]:
            return nums[:k]
        
        if x >= nums[-1]:
            return nums[-k:]
        
        def diff(num):
            return abs(x - num)
        
        def getKClosest(l, r):
            nonlocal k
            left, right = [], []
            while k:
                if l >= 0 and r < N:
                    if diff(nums[l]) <= diff(nums[r]):
                        left.append(nums[l])
                        l -= 1
                    else:
                        right.append(nums[r])
                        r += 1
                elif l >= 0:
                    left.append(nums[l])
                    l -= 1
                else:
                    right.append(nums[r])
                    r += 1

                k -= 1
                
            return left[::-1] + right
        
        l, r = 0, N-1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == x:
                return getKClosest(mid, mid+1)
            elif nums[mid] < x and mid < N-1 and nums[mid+1] > x:
                return getKClosest(mid, mid+1)
            elif nums[mid] > x and mid > 0 and nums[mid-1] < x:
                return getKClosest(mid-1, mid)
            elif nums[mid] < x:
                l = mid+1
            else:
                r = mid-1
                

# Optimal binary search
class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(A) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]
 

# Heap based suboptimal solution
from heapq import heappush, heappop

class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        def diff(num):
            return abs(x - num)
            
        heap = [(-diff(A[0]), A[0])]
        for i in range(1, len(A)):
            if len(heap) < k:
                heappush(heap, (-diff(A[i]), A[i]))
            elif (currDiff:= diff(A[i])) < -heap[0][0]:
                heappop(heap)
                heappush(heap, (-currDiff, A[i]))
                
        return sorted([x[1] for x in heap])
                
