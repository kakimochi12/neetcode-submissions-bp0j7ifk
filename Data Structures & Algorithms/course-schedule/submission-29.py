class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevmap = [[] for i in range(numCourses)]

        for crs, pre in prerequisites:
            prevmap[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if prevmap[crs] == []:
                return True
            
            visited.add(crs)
            for nei in prevmap[crs]:
                if not dfs(nei):
                    return False

            visited.remove(crs)
            prevmap[crs] = []
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True