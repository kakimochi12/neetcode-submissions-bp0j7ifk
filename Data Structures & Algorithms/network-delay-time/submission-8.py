class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        t = 0
        visit = set()

        while minHeap:
            t1, v1 = heapq.heappop(minHeap)
            if v1 in visit:
                continue
            visit.add(v1)
            t = t1
            for v2, t2 in edges[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (t1 + t2, v2))
        return t if len(visit) == n else -1