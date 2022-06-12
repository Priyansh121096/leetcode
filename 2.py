# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nh = ListNode()
        
        curr, c1, c2 = nh, l1, l2
        carry = 0
        while c1 or c2:
            ns = carry + (0 if not c1 else c1.val) + (0 if not c2 else c2.val)
            #print(ns, carry)
            if ns >= 10:
                carry = 1
                ns -= 10
            else:
                carry = 0
            curr.val = ns
            
            c1 = None if not c1 else c1.next
            c2 = None if not c2 else c2.next
            if not (c1 or c2):
                if carry:
                    curr.next = ListNode(carry)
                
                return nh
            
            curr.next = ListNode()
            curr = curr.next
            
        return nh


# Space optimized
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev, c1, c2 = None, l1, l2
        carry = 0
        while c1 or c2:
            # Calculate the new sum.
            ns = carry + (0 if not c1 else c1.val) + (0 if not c2 else c2.val)
            if ns >= 10:
                carry = 1
                ns -= 10
            else:
                carry = 0
            
            # Store new sums in c1 instead of a new list.
            c1.val = ns
            
            # If c1 is empty before c2; use c2's nodes by attaching
            # them to c1 and removing them from c2 (to prevent double
            # counting).
            prev = c1
            if not c1.next and c2 and c2.next:
                c1.next = c2.next
                c2.next = None
            
            c1 = None if not c1 else c1.next
            c2 = None if not c2 else c2.next
            if not (c1 or c2):
                break
            
        # If there's a left-over carry; create a new node with the carry.
        if carry:
            prev.next = ListNode(carry)

        return l1