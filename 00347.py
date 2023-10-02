# https://leetcode.com/problems/top-k-frequent-elements/
# 347. Top K Frequent Elements


# Heap based
from heapq import heapify, nlargest
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = [(c[num], num) for num in c]
        return [x[1] for x in nlargest(k, heap)]


# Bucket sort on frequencies.
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c, mfreq = defaultdict(int), -inf
        for num in nums:
            c[num] += 1
            mfreq = max(mfreq, c[num])
        
        freq = [None for _ in range(mfreq+1)]
        
        for num, f in c.items():
            if freq[f] is not None:
                freq[f].add(num)
            else:
                freq[f] = {num}
            
        out = []
        for i in range(mfreq, -1, -1):
            if freq[i] is not None:
                if len(freq[i]) <= k:
                    out.extend(list(freq[i]))
                    k -= len(freq[i])
                else:
                    out.extend(list(freq[:k]))
                    break
                
        return out
