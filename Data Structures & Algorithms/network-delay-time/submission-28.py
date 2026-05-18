class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = set()
        time = 0
        while minHeap:
            t1, u = heapq.heappop(minHeap)
            if u in visited:
                continue
            
            visited.add(u)
            time = t1
            for v, t2 in edges[u]:
                heapq.heappush(minHeap, (t1+t2, v))
        return time if len(visited) == n else -1