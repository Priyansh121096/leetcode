# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# 863. All Nodes Distance K in Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def setParent(node, parent):
            if not node:
                return
            
            node.parent = parent    
            setParent(node.left, node)
            setParent(node.right, node)
        
        setParent(root, None)
        
        queue = [target]
        visited = set()
        count = 0
        while queue and count < k:
            new_queue = []
            for curr in queue:
                visited.add(curr)
                if curr.left not in visited and curr.left:
                    new_queue.append(curr.left)
                if curr.right not in visited and curr.right:
                    new_queue.append(curr.right)
                if curr.parent not in visited and curr.parent:
                    new_queue.append(curr.parent)
                    
            queue = new_queue
            count += 1
            
        return [x.val for x in queue] if count == k else []