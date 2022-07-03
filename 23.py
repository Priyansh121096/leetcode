# https://leetcode.com/problems/merge-k-sorted-lists/
# 23. Merge k Sorted Lists

from heapq import heapify, heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        heap = [(head.val, i) for i, head in enumerate(lists) if head is not None]
        if not heap:
            return
        heapify(heap)
        
        # Get the head of the new LL
        _, headi = heappop(heap)
        head = lists[headi]
        lists[headi] = head.next
        if lists[headi]:
            heappush(heap, (lists[headi].val, headi))
        curr = head
        
        # Merge 
        while heap:
            _, nxti = heappop(heap)
            curr.next = lists[nxti]
            lists[nxti] = lists[nxti].next
            if lists[nxti]:
                heappush(heap, (lists[nxti].val, nxti))
            curr = curr.next
            
        return head
            