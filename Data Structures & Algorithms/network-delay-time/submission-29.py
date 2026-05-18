class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))

        minHeap = [(0, k)]
        t = 0
        visited = set()

        while minHeap:
            t1, u = heapq.heappop(minHeap)
            if u in visited:
                continue

            t = t1
            visited.add(u)
            for v, t2 in edges[u]:
                heapq.heappush(minHeap, (t1+t2, v))
        return t if len(visited) == n else -1