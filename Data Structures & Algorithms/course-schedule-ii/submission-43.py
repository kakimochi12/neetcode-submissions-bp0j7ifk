class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visited = set()
        res = []
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            
            for nei in premap[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        for n in range(numCourses):
            if not dfs(n):
                return []
        return res
