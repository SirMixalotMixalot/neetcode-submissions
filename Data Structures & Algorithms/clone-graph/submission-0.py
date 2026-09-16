"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.seen = set()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        currentNodes = {}
        def dfs(node):
            if node in currentNodes:
                return currentNodes[node]
            
            copy = Node(node.val)

            currentNodes[node] = copy 
            for c in node.neighbors:
                copy.neighbors.append(dfs(c))
            return copy
        return dfs(node) if node else None
        
        
        