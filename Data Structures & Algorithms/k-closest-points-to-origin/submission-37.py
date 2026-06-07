class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        res = []

        for i in range(len(points)):
            x, y = points[i]
            dist = x**2 + y**2
            store.append([dist, [x, y]])

        heapq.heapify(store)
        while k > 0:
            val = heapq.heappop(store)[1]
            res.append(val)
            k -= 1
        return res