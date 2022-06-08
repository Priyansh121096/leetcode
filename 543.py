# https://leetcode.com/problems/diameter-of-binary-tree/
# 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, height):
        if not node:
            return 0, 0
        
        if not (node.left or node.right):
            return 1, 0
        
        lh, ld = self.dfs(node.left, height)
        rh, rd = self.dfs(node.right, height)
        
        height = max(lh, rh) + 1
        diameter = max(ld, rd, lh+rh)
        
        return height, diameter
        
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)[1]
        
        