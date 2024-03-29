# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 235. Lowest Common Ancestor of a Binary Search Tree

# Solution 1 (Sub-optimal)
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAncestorsOfNode(self, root, node, anc):
        if not root:
            return anc
        
        anc.append(root)
        
        if root is node:
            return anc
        
        if root.val > node.val:
            return self.getAncestorsOfNode(root.left, node, anc)
        
        return self.getAncestorsOfNode(root.right, node, anc)
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anc1 = self.getAncestorsOfNode(root, p, deque([]))
        anc2 = self.getAncestorsOfNode(root, q, deque([]))
        
        prev = None
        while anc1 and anc2 and (curr:= anc1.popleft()) == anc2.popleft():
            prev = curr
            
        return prev


# Solution 2 (Optimal)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        if p.val > q.val:
            p, q = q, p
        while lca:
            if p.val <= lca.val <= q.val:
                return lca
            
            if p.val <= lca.val and q.val <= lca.val:
                lca = lca.left
            else:
                lca = lca.right
                
        
        