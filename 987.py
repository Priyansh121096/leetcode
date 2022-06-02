# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# 987. Vertical Order Traversal of a Binary Tree

# Solution 1 (AC)
from bisect import insort_left

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, vlevel, hlevel):
        if not node:
            return
    
        self.minLevel = min(self.minLevel, vlevel)
        self.maxLevel = max(self.maxLevel, vlevel)
        
		# While inserting, give priority to hlevel (row) and then the value (node.val)
        insort_left(self.nodes[vlevel], (hlevel, node.val), key=lambda x: x[0]*1000 + x[1])
        
        self.helper(node.left, vlevel-1, hlevel+1)
        self.helper(node.right, vlevel+1, hlevel+1)
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.minLevel, self.maxLevel = inf, -inf
        self.nodes = [[] for _ in range(1000)]
        self.helper(root, 0, 0)

        ans = []
        if self.minLevel < 0:
            ans += [[x[1] for x in nodes] for nodes in self.nodes[self.minLevel:]]
        if self.maxLevel >= 0:
            ans += [[x[1] for x in nodes] for nodes in self.nodes[:self.maxLevel+1]]
        
        return ans