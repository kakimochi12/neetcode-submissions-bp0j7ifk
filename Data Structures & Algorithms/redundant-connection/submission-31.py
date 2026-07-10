class DSU:
    def __init__(self, n):
        self.Parent = list(range(n+1))
        self.child = [0] * (n+1)
    def find(self, node):
        if node != self.Parent[node]:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.child[pu] >= self.child[pv]:
            self.Parent[pv] = pu
            self.child[pu] += self.child[pv]
        else:
            self.Parent[pu] = pv
            self.chuld[pv] += self.child[pu]
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]