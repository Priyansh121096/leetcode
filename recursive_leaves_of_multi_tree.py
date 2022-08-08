# https://leetcode.com/discuss/interview-question/1693416/google-onsite-recursively-delete-leave-nodes-in-a-multi-tree
# https://leetcode.com/playground/45sMRiqx

from sortedcontainers import SortedDict

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def assign_heights(node: Node, nodes: dict) -> int:
    if not node:
        return float('-inf')

    if not node.children:
        if 0 in nodes:
            nodes[0].append(node.val)
        else:
            nodes[0] = [node.val]
        return 0

    maxHeight = float('-inf')
    for child in node.children:
        currHeight = assign_heights(child, nodes)
        maxHeight = max(maxHeight, currHeight)
    
    if maxHeight+1 in nodes:
        nodes[maxHeight+1].append(node.val)
    else:
        nodes[maxHeight+1] = [node.val]
    return maxHeight + 1

def get_leaves_recursively(root: Node) -> list:
    nodes = SortedDict({})
    rootHeight = assign_heights(root, nodes)

    return [leaf for level in nodes.values() for leaf in level]

def main():
    nodes = [Node(i+1) for i in range(8)]

    nodes[0].children = [nodes[1], nodes[2], nodes[3]]
    nodes[1].children = [nodes[4], nodes[5]]
    nodes[2].children = [nodes[6]]
    nodes[5].children = [nodes[7]]

    print(get_leaves_recursively(nodes[0]))

if __name__ == "__main__":
    main()