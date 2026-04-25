class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        store = []
        for s in stones:
            store.append(-s)
        
        heapq.heapify(store)
        while len(store) > 1:
            s1 = -heapq.heappop(store)
            s2 = -heapq.heappop(store)
            heapq.heappush(store, -abs(s1 - s2))
        return -store[0]