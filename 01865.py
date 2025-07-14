# 1865. Finding Pairs With a Certain Sum

from collections import Counter
import bisect

from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.c1 = Counter(nums1)
        
        self.nums2 = nums2
        self.c2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.nums2[index] = new_val

        self.c2[old_val] -= 1
        self.c2[new_val] += 1

    def count(self, tot: int) -> int:
        count = 0
        for val in self.c1:
            look_for = tot - val
            count += self.c1[val] * self.c2[look_for]

        return count

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.x = sorted(nums1)
        
        self.y = nums2
        self.cy = Counter(nums2)
        self.yMax = max(self.cy.keys())

    def add(self, index: int, val: int) -> None:
        old_val = self.y[index]
        new_val = old_val + val
        self.y[index] = new_val

        self.cy[old_val] -= 1
        self.cy[new_val] += 1
        self.yMax = max(self.yMax, new_val)

    def count(self, tot: int) -> int:
        # Find the minimum index in X from where to begin the search
        # This is because X values less than minX (tot - yMax) will never
        # find a corresponding Y value because they'll need to be greater
        # than yMax.
        # This takes O(logn) using binary search since X is sorted during initialization
        minX = tot - self.yMax
        minIdx = bisect.bisect_left(self.x, minX)

        count = 0
        for idx in range(minIdx, len(self.x)):
            look_for = tot - self.x[idx]
            count += self.cy[look_for]

        return count

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
