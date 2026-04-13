class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n:
            return False
        
        prevmap = [[] for i in range(n)]
        for u, v in edges:
            prevmap[u].append(v)
            prevmap[v].append(u)
        
        visited = set()
        def dfs(node, par):
            if node in visited:
                return False

            visited.add(node)
            for nei in prevmap[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n