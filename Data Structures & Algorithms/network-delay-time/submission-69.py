class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append([v, t])

        res = 0
        minHeap = [(0, k)]
        visited = set()
        while minHeap:
            t1, u = heapq.heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            res = t1
            for v, t2 in adj[u]:
                heapq.heappush(minHeap, [t1+t2, v])
        return res if len(visited) == n else -1
