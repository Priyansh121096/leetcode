# https://leetcode.com/problems/path-sum-ii/
# 113. Path Sum II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        out = []
        def dfs(node, currSum, currPath):
            if not node:
                return False
            
            if not node.left and not node.right:
                if currSum == targetSum:
                    out.append(currPath[:])
                
                return 
            
            if node.left:
                currPath.append(node.left.val)
                dfs(node.left, currSum + node.left.val, currPath)
                currPath.pop()
                
            if node.right:
                currPath.append(node.right.val)
                dfs(node.right, currSum + node.right.val, currPath)
                currPath.pop()
        
        dfs(root, root.val, [root.val])
        
        return out