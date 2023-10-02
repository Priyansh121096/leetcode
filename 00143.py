# https://leetcode.com/problems/reorder-list/
# 143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
            
        N = len(stack)
        curr = head
        for i in range(N//2):
            nxt = curr.next
            last = stack.pop()
            curr.next = last
            last.next = nxt
            curr = nxt
            
        if N % 2 != 0:
            curr.next = stack.pop()
            curr.next.next = None
        else:
            curr.next = None
            
        return head

# O(1) space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        
        # Reach the middle
        sp, fp = head, head
        while fp.next and fp.next.next:
            sp = sp.next
            fp = fp.next.next
            
        if fp.next:
            sp = sp.next
            fp = fp.next
            
        # Reverse the LL starting from the SP
        mid, prev, curr = sp, None, sp
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Join last with first till we reach mid
        first, last = head, fp
        while first != mid:
            fwd, back = first.next, last.next
            first.next = last
            last.next = fwd
            first, last = fwd, back
        
        mid.next = None
    
        return head