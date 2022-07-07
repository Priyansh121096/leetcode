# https://leetcode.com/problems/implement-trie-prefix-tree/
# 208. Implement Trie (Prefix Tree)

class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        lastNode = self.lastNode(word)
            
        return lastNode is not None and lastNode.isEnd
    
    def lastNode(self, prefix):
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return None
            curr = curr.children[w]
            
        return curr

    def startsWith(self, prefix: str) -> bool:
        lastNode = self.lastNode(prefix)
        
        return lastNode is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)