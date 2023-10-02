# https://leetcode.com/problems/merge-sorted-array/
# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], M: int, nums2: List[int], N: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if N == 0:
            return
        
        if M == 0:
            for i, num in enumerate(nums2):
                nums1[i] = num
            return
        
        p1, p2, p = M-1, N-1, (M+N-1)
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
                
        #print(p1, p2, p)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
            
        while p1 >= 0:
            nums1[p] = nums1[p1]
            p -= 1
            p1 -= 1
                