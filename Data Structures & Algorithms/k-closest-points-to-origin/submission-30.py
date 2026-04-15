class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        store = []

        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(store, [dist, [x, y]])
        
        while k > 0:
            res.append(heapq.heappop(store)[1])
            k -= 1
        return res