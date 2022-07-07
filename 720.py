# https://leetcode.com/problems/longest-word-in-dictionary/
# 720. Longest Word in Dictionary

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

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        def longestPath(node, path):
            maxPathLen, maxPath = len(path), path
            for i in range(26):
                letter = chr(ord('a') + i) 
                child = node.children.get(letter, None)
                if not child or not child.isEnd:
                    continue
                
                currPath = longestPath(child, path + [letter])
                
                if len(currPath) > maxPathLen:
                    maxPathLen = len(currPath)
                    maxPath = currPath
                    
            return maxPath

        maxPath = longestPath(trie.root, [])

        return "" if not maxPath else "".join(maxPath)
