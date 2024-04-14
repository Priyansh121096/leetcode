# https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q, sumL = deque([root]), 0
        while q:
            curr = q.popleft()
            if curr.left:
                if not (curr.left.left or curr.left.right):
                    sumL += curr.left.val
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return sumL


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], sumL=0, is_left=False) -> int:
        if not root:
            return sumL

        if not (root.left or root.right):
            if is_left:
                sumL += root.val
            return sumL

        return self.sumOfLeftLeaves(root.left, sumL, True) + self.sumOfLeftLeaves(root.right, sumL, False)
