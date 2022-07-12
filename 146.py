# https://leetcode.com/problems/lru-cache/
# 146. LRU Cache

class Node:
    def __init__(self, key, val, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
        
    def _remove(self, node):
        """Remove from middle"""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        
    def _insert(self, node):
        """Insert before right"""
        prevprev = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev = prevprev
        prevprev.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        
        # Remove node from middle of LL and put itb before right
        self._remove(node)
        self._insert(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
        
        if not node:
            node = Node(key, value)
            self.map[key] = node
            
        self._insert(node)
        
        if len(self.map) > self.cap:
            del self.map[self.left.next.key]
            self._remove(self.left.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)