# https://leetcode.com/problems/linked-list-cycle-ii/
# 142. Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        sp, fp = head, head
        while sp and fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if sp is fp:
                break
        else:
            return None
        
        sp = head
        while sp is not fp:
            sp = sp.next
            fp = fp.next
            
        return sp
            