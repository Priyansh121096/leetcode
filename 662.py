# https://leetcode.com/problems/maximum-width-of-binary-tree/
# 662. Maximum Width of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [[root, 1]]
        maxWidth = 1
        
        while queue:
            new_queue = []
            maxWidth = max(maxWidth, queue[-1][1] - queue[0][1] + 1)
            for curr, currIdx in queue:
                if curr.left:
                    new_queue.append([curr.left, currIdx*2])
                if curr.right:
                    new_queue.append([curr.right, currIdx*2+1])
                    
            queue = new_queue
                    
        return maxWidth
        