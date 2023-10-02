# https://leetcode.com/problems/validate-binary-search-tree/
# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root, lessThan=inf, largerThan=-inf):
        if not root:
            return True
        
        if root.val <= largerThan or root.val >= lessThan:
            return False
        
        return (self.isValidBST(root.left, min(lessThan, root.val), largerThan) 
                and self.isValidBST(root.right, lessThan, max(root.val, largerThan)))