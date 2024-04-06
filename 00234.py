# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self, head):
        # O(N)
        c = 0
        while head:
            c += 1
            head = head.next
        return c

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """O(N) time and O(1) space"""
        if not head or not head.next:
            return True

        if not head.next.next:
            return head.val == head.next.val

        # Get the length of the list
        N = self.get_len(head)

        # Reverse the left half of the LL
        curr, nxt = None, head
        for i in range((N//2) if N%2 == 0 else N//2+1):
            nxtnxt = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = nxtnxt

        # Compare the left half of the linked list with the
        # right half one node at a time. If it's an odd-length
        # list, skip the middle element (curr)
        lh, rh = (curr if N%2 == 0 else curr.next), nxt
        while lh and rh:
            if lh.val != rh.val:
                return False
            lh, rh = lh.next, rh.next
        
        # Both left and right pointers should be None at the end.
        return not (lh or rh)
