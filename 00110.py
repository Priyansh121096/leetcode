# https://leetcode.com/problems/balanced-binary-tree/
# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        
        def dfs(root, currDepth):
            nonlocal isBalanced
            
            if not root:
                return currDepth
            
            if not root.left and not root.right:
                return currDepth + 1

            leftDepth = dfs(root.left, currDepth+1)
            rightDepth = dfs(root.right, currDepth+1)
            
            if abs(leftDepth - rightDepth) > 1:
                isBalanced = False
                
            return max(leftDepth, rightDepth)
        
        dfs(root, 0)
        
        return isBalanced