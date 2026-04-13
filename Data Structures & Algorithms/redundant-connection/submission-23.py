class DSU:
    def __init__(self, n):
        self.Parent = list(range(n+1))
        self.rank = [0] * (n+1)
    def find(self, node):
        if node != self.Parent[node]:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False

        if self.rank[pu] >= self.rank[pv]:
            self.Parent[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.Parent[pu] = pv
            self.rank[pv] += self.rank[pu]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]