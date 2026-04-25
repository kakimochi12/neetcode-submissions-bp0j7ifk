class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = [[] for i in range(numCourses)]

        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if premap[crs] == []:
                return True
            
            visited.add(crs)
            for nei in premap[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)
            premap[crs] = []
            return True
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True