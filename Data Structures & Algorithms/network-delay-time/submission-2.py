class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))

        minHeap = [(0, k)]  # time, node
        visit = set()
        t = 0
        while minHeap:
            time, u = heapq.heappop(minHeap)
            if u in visit:
                continue
            visit.add(u)

            t = time
            for vnew, tnew in edges[u]:
                if vnew not in visit:
                    heapq.heappush(minHeap, [tnew + time, vnew])
        return t if len(visit) == n else -1


            