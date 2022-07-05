# https://leetcode.com/problems/reverse-linked-list-ii/
# 92. Reverse Linked List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        front, back = None, None
        curr = head
        n = 1
        while curr:
            if n == left-1:
                front = curr
            if n == right+1:
                back = curr
            curr = curr.next
            n += 1

        end = front.next if front else head
        prev, curr = None, front.next if front else head
        while curr is not back:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        if front is None and back is None:
            return prev
        
        if front is None:
            end.next = back
            return prev
        
        end.next = back
        front.next = prev
            
        return head
            
            
# Single pass
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        # Find front
        curr, front = head, None
        if left > 1:
            for i in range(left-2):
                curr = curr.next
            front = curr
       
        # Reverse the middle
        n = left
        prev, curr, mid_end = None, head if front is None else front.next, head if front is None else front.next
        while n != right+1:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            n += 1
        
        middle, back = prev, curr

        if front is None and back is None:
            return prev
        
        # Attach back to middle's end
        mid_end.next = back
        if front is None:
            return prev

        # Attach middle's start to front
        front.next = middle
            
        return head