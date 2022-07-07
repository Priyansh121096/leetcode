# https://leetcode.com/problems/path-sum/
# 112. Path Sum

# DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False
            
            if not node.left and not node.right:
                return (currSum + node.val) == targetSum
            
            return dfs(node.left, currSum+node.val) or dfs(node.right, currSum+node.val)
        
        return root and dfs(root, 0)

# BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return 
        
        queue = [(root, root.val)]
        while queue:
            new_queue = []
            for curr, currSum in queue:
                is_leaf = True
                
                if curr.left:
                    is_leaf = False
                    new_queue.append((curr.left, currSum + curr.left.val))
                    
                if curr.right:
                    is_leaf = False
                    new_queue.append((curr.right, currSum + curr.right.val))
                    
                if is_leaf and currSum == targetSum:
                    return True
                
            queue = new_queue
                
        return False
                