# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = [root]
        out = []
        while q:
            out.append([node.val for node in q])
            newq = []
            for node in q:
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            q = newq
            
        return out
        