# https://leetcode.com/problems/linked-list-cycle/
# 141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


# Reverse LL. It'll reach head if cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        prev, curr = head, head.next
        while curr:
            if curr is head:
                return True
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return False