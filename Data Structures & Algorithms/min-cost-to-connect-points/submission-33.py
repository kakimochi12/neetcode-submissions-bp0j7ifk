class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        minHeap = [[0, 0]]
        visited = set()
        res = 0

        while minHeap:
            neiCost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res += neiCost
            for cost, w in adj[node]:
                if not w in visited:
                    heapq.heappush(minHeap, (cost, w))
        return res