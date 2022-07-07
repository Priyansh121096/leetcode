# https://leetcode.com/problems/path-sum-iii/
# 437. Path Sum III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        numPaths = 0
        
        def dfs(node, ancestors):
            nonlocal numPaths
            
            if not node:
                return
            
            currSum = node.val
            
            if currSum == targetSum:
                numPaths += 1
                
            for i in range(len(ancestors)-1, -1, -1):
                currSum += ancestors[i]
                if currSum == targetSum:
                    numPaths += 1
                    
            ancestors.append(node.val)       
            dfs(node.left, ancestors)
            dfs(node.right, ancestors)
            ancestors.pop()
                
        dfs(root, [])
        return numPaths
        