# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# 430. Flatten a Multilevel Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def getFlatHeadTail(head, tail):
            if not head:
                return None, None

            if not head.next and not head.child:
                return head, tail
            
            if not head.child:
                nextFlatNodeHead, nextFlatNodeTail = getFlatHeadTail(head.next, tail)
                head.next = nextFlatNodeHead
                nextFlatNodeHead.prev = head
                return head, nextFlatNodeTail
            
            childHead = head.child
            childTail = childHead
            while childTail.next:
                childTail = childTail.next

            flattenedChildHead, flattenedChildTail = getFlatHeadTail(childHead, childTail)

            if not head.next:
                head.next = flattenedChildHead
                flattenedChildHead.prev = head
                head.child = None
                return head, flattenedChildTail
            
            nextFlatNodeHead, nextFlatNodeTail = getFlatHeadTail(head.next, tail)
        
            head.child = None
            head.next = flattenedChildHead
            flattenedChildHead.prev = head
            
            flattenedChildTail.next = nextFlatNodeHead
            nextFlatNodeHead.prev = flattenedChildTail
            
            return head, nextFlatNodeTail
            
        tail = head
        while tail and tail.next:
            tail = tail.next
            
        return getFlatHeadTail(head, tail)[0]