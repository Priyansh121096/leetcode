from operator import itemgetter

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
        
        self.nodes[vlevel].append((hlevel, node.val))
        
        self.helper(node.left, vlevel-1, hlevel+1)
        self.helper(node.right, vlevel+1, hlevel+1)
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.minLevel, self.maxLevel = inf, -inf
        self.nodes = [[] for _ in range(1000)]
        self.helper(root, 0, 0)

        ans = []
        if self.minLevel < 0:
            ans += [[x[1] for x in sorted(nodes, key=itemgetter(0))] for nodes in self.nodes[self.minLevel:]]
        if self.maxLevel >= 0:
            ans += [[x[1] for x in sorted(nodes, key=itemgetter(0))] for nodes in self.nodes[:self.maxLevel+1]]
        
        return ans