# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        from_left = True
        out = []
        while queue:
            new_queue = []
            vals = []
            for curr in queue:
                vals.append(curr.val)
                if curr.left:
                    new_queue.append(curr.left)
                if curr.right:
                    new_queue.append(curr.right)
                    
            out.append(vals if from_left else vals[::-1])
            queue = new_queue
            from_left = not from_left
            
        return out
            