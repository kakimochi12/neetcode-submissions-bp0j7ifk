"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtocopy = {None:None}

        def dfs(node):
            if node in oldtocopy:
                return oldtocopy[node]
            curr = Node(node.val)
            oldtocopy[node] = curr
            for nei in node.neighbors:
                curr.neighbors.append(dfs(nei))
            return curr
        return dfs(node) 
        