class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u1, v1, t1 in times:
            edges[u1].append((v1, t1))

        minHeap = [(0, k)]
        t = 0
        visit = set()

        while minHeap:
            t2, u2 = heapq.heappop(minHeap)
            if u2 in visit:
                continue
            visit.add(u2)
            t = t2
            for v2, t3 in edges[u2]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (t2 + t3, v2))
        return t if len(visit) == n else -1