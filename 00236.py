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
        # If it's a null node, return None
        # If you've reached either of p and q, that node is the LCA
        # between p and q in the subtree rooted at p or q.
        if root in (None, p, q):
            return root
        
        # Find LCAs of p and q in the left and the right subtrees.
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        
        # If neither of them exists, it means we weren't able to p and q in any subtree.
        if not left and not right:
            return 
        
        # If both exist, it means we found p in one subtree and q in the other. So, LCA is root.
        if left and right:
            return root
        
        # If only one of them exists, it means we found both p and q in either the left or the right
        # subtree. This means the LCA is either the left or the right (whichever is non-null.)
        return left or right
