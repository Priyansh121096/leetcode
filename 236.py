# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, tgt, path):
            if node is tgt:
                return path + [tgt]
            
            if not node:
                return
            
            lpath = dfs(node.left, tgt, path + [node])
            if lpath:
                return lpath
            
            rpath = dfs(node.right, tgt, path + [node])
            return rpath
        
        ppath, qpath = dfs(root, p, []), dfs(root, q, [])
        
        i = 0
        while i < len(ppath) and i < len(qpath) and ppath[i] is qpath[i]:
            i += 1
            
        return ppath[i-1]

# Optimal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        
        if not left and not right:
            return 
        
        if left and right:
            return root
        
        return left or right