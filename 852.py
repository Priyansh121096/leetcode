# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# 852. Peak Index in a Mountain Array

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #print('---')
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l + r) // 2
            #print(l, m, r)
            if m == 0 and arr[m] > arr[m+1]:
                return m
            elif m == len(arr)-1 and arr[m-1] < arr[m]:
                return m
            elif (arr[m-1] < arr[m]) and (arr[m] > arr[m+1]):
                return m
            elif arr[m-1] < arr[m]:
                l = m
            else:
                r = m
                