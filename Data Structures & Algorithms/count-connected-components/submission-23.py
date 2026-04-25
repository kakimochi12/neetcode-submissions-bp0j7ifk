class DSU:
    def __init__(self, n):
        self.Parent = list(range(n))
        self.rank = [0] * n
    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] >= self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.Parent[pv] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.Parent[pu] = pv
        return True
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n

        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res