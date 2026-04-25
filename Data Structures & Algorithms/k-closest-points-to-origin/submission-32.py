class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        res = []

        for x, y in points:
            dist = x **2 + y ** 2
            heapq.heappush(store, [dist, [x, y]])
        
        while len(res) < k:
            val = heapq.heappop(store)[1]
            res.append(val)
        return res