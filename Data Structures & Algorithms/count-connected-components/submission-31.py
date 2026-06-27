class DSU:
    def __init__(self, n):
        self.Parent = list(range(n))
        self.child = [0] * n
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
            self.child[pv] = pu
        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)

        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res