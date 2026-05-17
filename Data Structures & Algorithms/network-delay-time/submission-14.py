class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge = defaultdict(list)

        for u, v, t in times:
            edge[u].append((v, t))

        minHeap = [(0, k)] #(time, node)
        visited = set()
        t = 0
        while minHeap:
            t1, u = heapq.heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            t = t1
            for v, t2 in edge[u]:
                if v not in visited:
                    heapq.heappush(minHeap, (t1 + t2, v))
        return t if len(visited) == n else -1
