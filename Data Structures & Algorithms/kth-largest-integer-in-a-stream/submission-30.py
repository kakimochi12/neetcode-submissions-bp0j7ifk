class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store = nums
        heapq.heapify(self.store)
        self.k = k

        while len(self.store) > self.k:
            heapq.heappop(self.store)
    def add(self, val: int) -> int:
        heapq.heappush(self.store, val)

        if len(self.store) > self.k:
            heapq.heappop(self.store)
        return self.store[0]
        
