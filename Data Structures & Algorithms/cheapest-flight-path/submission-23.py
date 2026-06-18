class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for i in range(n)]

        for u, v, t in flights:
            adj[u].append((v, t))

        q = deque([(0, src, 0)])
        while q:
            cost, place, flights = q.popleft()
            if flights > k:
                continue
            for nei, w in adj[place]:
                newCost = w + cost
                if newCost < prices[nei]:
                    prices[nei] = newCost
                    q.append([newCost, nei, flights + 1])
        return prices[dst] if prices[dst] != float("inf") else -1