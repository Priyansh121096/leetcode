# https://leetcode.com/playground/nEqyHQ3X

"""
https://leetcode.com/discuss/interview-question/2199394/Google-or-Phone-or-Time-for-turn
Problem description
Joseph is standing at k+1th position in a queue at an insurance company's office 
and there are n counters at the office, ith counter takes time[i] time (minutes) 
to process a request. The security guard assigns a counter to the person standing 
in the front of the queue as soon as a counter is available or if multiple counters
are available, then the security official assigns the counter with minimum id 
(consider id as index). What would be the time at which Joseph's request would be 
processed aka the ending time when Joseph leaves the office?

Examples
Input: time=[3,2,5], k=4
Output: 6
Explanation: Joseph is standing at 5th position (1-indexed). Initially, all counters
are empty so people at positions 1-3 are put to the respective counters. After 2 
minutes, counter 2 (1-indexed) gets empty and person at position 4 is assigned to the 
counter. After 1 more minute, counter 1 gets empty and now Joseph is assigned the 
counter 1. Joseph leaves after 3 minutes from the counter. So, in total, Joseph spends 
6 minutes in the office.
"""
from heapq import heappush, heappop, heapify

def timeForTurn(n, times, k):
    if n > k:
        return times[k]
    
    heap = [(time, i) for i, time in enumerate(times)]
    heapify(heap)

    for j in range(k-n):
        etime, index = heappop(heap)
        new_etime = etime + times[index]
        heappush(heap, (new_etime, index))

    etime, index = heappop(heap)
    return etime + times[index]

def main():
    print(timeForTurn(3, [3,2,5], 4))  # 6
    print(timeForTurn(3, [3,2,5], 3))  # 4
    print(timeForTurn(3, [3,2,5], 2))  # 5

if __name__ == "__main__":
    main()