# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, maxSum):
        if not node:
            return -inf, maxSum

        sumLeft, maxSum = self.dfs(node.left, maxSum)
        sumRight, maxSum = self.dfs(node.right, maxSum)
        currSum = max(sumLeft, 0) + max(sumRight, 0) + node.val
        maxSum = max(maxSum, currSum)

        return max(sumLeft, sumRight, 0) + node.val, maxSum
        
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val)[1]
