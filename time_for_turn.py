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
"""
from heapq import heappush, heappop, heapify


def timeForTurn(n, times, k):
    if n > k:
        return 0

    def key(etime, index):
        return etime * (10**6) + index 

    def unkey(val):
        index = val % (10**6)
        etime = (val - index) // (10**6)
        return etime, index

    heap = [key(time, i) for i, time in enumerate(times)]
    heapify(heap)

    for j in range(k-n):
        etime, index = unkey(heappop(heap))
        new_etime = etime + times[index]
        heappush(heap, key(new_etime, index))

    etime, index = unkey(heappop(heap))
    return etime + times[index]


def main():
    n = 3
    times = [3,2,5]
    k = 4
    print(timeForTurn(n, times, k))


if __name__ == "__main__":
    main()