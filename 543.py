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
        """
        :returns: A 2-tuple (height, diameter) of the subtree rooted at `node`.
        """
        if not node:
            # Node is NULL; height and diameter are 0.
            return 0, 0

        if not (node.left or node.right):
            # Node has no children; height is 1; diameter is 0.
            return 1, 0

        # Get heights and diameters of left and right subtrees.
        lh, ld = self.dfs(node.left, height)
        rh, rd = self.dfs(node.right, height)

        # Height of the subtree rooted at `node` is 1 plus the
        # maximum of the heights of left and right subtrees.
        height = max(lh, rh) + 1

        # Diameter of the subtree rooted at `node` is the maximum of:
        # A) The diameter of left subtree
        # B) The diameter of right subtree
        # C) The sum of the heights of left and right subtrees.
        # If the max is C, it means that the diametric path goes through `node`.
        diameter = max(ld, rd, lh+rh)

        return height, diameter
        
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)[1]
