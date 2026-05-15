class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            t1, u1 = heapq.heappop(minHeap)
            if u1 in visit:
                continue
            visit.add(u1)
            t = t1

            for v2, t2 in edges[u1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, [t1 + t2, v2])
        return t if len(visit) == n else -1
