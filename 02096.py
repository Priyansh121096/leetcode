# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# 2096. Step-By-Step Directions From a Binary Tree Node to Another

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def preorderFind(root, x, pre, path):
            if not root:
                return None, None
            
            if root.val == x:
                pre.append(x)
                return pre, path
              
            pre.append(root.val)
            path.append('L')
            preL, pathL = preorderFind(root.left, x, pre, path)
            if preL:
                return preL, pathL
            path.pop()
            
            path.append('R')
            preR, pathR = preorderFind(root.right, x, pre, path)
            if preR:
                return preR, pathR
            path.pop()
            
            pre.pop()
            
            return None, None
        
        # Do preorder traversals and paths of start and dest nodes.
        # These give us paths from root -> ... LCA ... -> start and root -> ... LCA ... -> dest.
        preS, pathS = preorderFind(root, startValue, [], [])
        preD, pathD = preorderFind(root, destValue, [], [])
        
        # Find LCA of start and dest (i-1 will be the LCA)
        i = 0
        while i < len(preS) and i < len(preD) and preS[i] == preD[i]:
            i += 1
            
        # Shortest path between start and dest is start -> LCA -> dest.
        # Reverse of LCA -> start will be UUUU... of the same length.
        for j in range(i-1, len(pathS)):
            pathS[j] = 'U'
        
        # We're not concerned about root but only the LCA.
        # Shortest path is start -> LCA + LCA -> dest.
        return "".join(pathS[i-1:] + pathD[i-1:])
        
        
        