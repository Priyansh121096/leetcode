# https://leetcode.com/problems/find-leaves-of-binary-tree/
# 366. Find Leaves of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def is_leaf(node):
            return not node.left and not node.right
        
        def removeAllLeaves(node):
            if not node:
                return []
            
            leftLeaves = []
            if node.left and not is_leaf(node.left):
                leftLeaves = removeAllLeaves(node.left)
            elif node.left:
                leftLeaves = [node.left.val]
                node.left = None
            
            rightLeaves = []
            if node.right and not is_leaf(node.right):
                rightLeaves = removeAllLeaves(node.right)
            elif node.right:
                rightLeaves = [node.right.val]
                node.right = None
            
            return leftLeaves + rightLeaves
            
        leaves = []
        while not is_leaf(root):
            currLeaves = removeAllLeaves(root)
            leaves.append(currLeaves)
            
        leaves.append([root.val])
        return leaves

# Better
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def is_leaf(node):
            return not node.left and not node.right
        
        leaves = [None for _ in range(100)]
        maxHeight = 0
        
        def assignHeights(node):
            nonlocal maxHeight
            
            if not node:
                return -1
            
            if is_leaf(node):
                if not leaves[0]:
                    leaves[0] = []
                    
                leaves[0].append(node.val)
                return 0
            
            leftHeight = assignHeights(node.left)
            rightHeight = assignHeights(node.right)
            height = max(leftHeight, rightHeight) + 1
            maxHeight = max(height, maxHeight)
            
            if not leaves[height]:
                leaves[height] = []
                
            leaves[height].append(node.val)
            return height
        
        assignHeights(root)
        
        return leaves[:maxHeight+1]


