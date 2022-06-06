# https://leetcode.com/problems/intersection-of-two-linked-lists/
# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: 
        currA, currB = headA, headB
        
        while currA != currB:
            currA = currA.next if currA is not None else headB
            currB = currB.next if currB is not None else headA
            
        return currA
            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: 
        currA = headA
        while currA:
            currA.flag = True
            currA = currA.next
            
        currB = headB
        while currB:
            if getattr(currB, 'flag', False):
                return currB
            currB = currB.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s1, s2 = [], []
        
        currA = headA
        while currA:
            s1.append(currA)
            currA = currA.next
            
        currB = headB
        while currB:
            s2.append(currB)
            currB = currB.next
            
        prev = None
        while s1 and s2 and s1[-1] is s2[-1]:
            s1.pop()
            prev = s2.pop()
            
        return prev