# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        ans = 0
        k = 1
        while stack:
            num = stack.pop()
            ans += num*k
            k *= 2

        return ans
