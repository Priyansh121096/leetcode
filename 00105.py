# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        inoIdx = inorder.index(root.val)
    
        root.left = self.buildTree(preorder[1:inoIdx+1], inorder[:inoIdx])
        root.right = self.buildTree(preorder[inoIdx+1:], inorder[inoIdx+1:])
        
        return root