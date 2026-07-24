class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited = set()
        cycle = set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res