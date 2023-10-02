# https://leetcode.com/problems/task-scheduler/
# 621. Task Scheduler

# Heap + waiting queue
from collections import Counter, deque
from heapq import heapify, heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        N = len(tasks)
        
        if n == 0:
            return N
        
        counts = Counter(tasks)
        max_heap = [(-count, char) for char, count in counts.items()]
        heapify(max_heap)
        
        queue = deque([])
        time = 0
        non_empty = 0
        while max_heap or non_empty > 0:
            time += 1

            if len(queue) == n+1:
                count, char = queue.popleft()
                if char is not None:
                    non_empty -= 1
                    heappush(max_heap, (-count, char))
                    
            if not max_heap:
                queue.append((None, None))
                continue
                
                
            count, char = heappop(max_heap)
            count = -count
            if count > 1:
                queue.append((count-1, char))
                non_empty += 1
            else:
                queue.append((None, None))
        
        return time


# Greedy approach using slot filling
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        N = len(tasks)
        
        if n == 0:
            return N
        
        maxFreq, maxCount = 0, 0
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
            if counts[task] == maxFreq:
                maxCount += 1
            elif counts[task] > maxFreq:
                maxCount = 1
                maxFreq = counts[task]
                
        numPartitions = maxFreq-1
        partitionLength = n - (maxCount-1)
        if partitionLength <= 0:
            return N
        
        emptySlots = numPartitions*partitionLength
        availableTasks = N - maxFreq*maxCount
        
        idleSlots = max(0, emptySlots-availableTasks)
        
        return N + idleSlots