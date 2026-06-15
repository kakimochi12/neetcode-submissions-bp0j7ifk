class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        visited.add((0, 0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == n-1 and c == n-1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr == n or nc == n or (nr, nc) in visited):
                    continue
                visited.add((nr, nc))
                heapq.heappush(minHeap, [max(grid[nr][nc], t), nr, nc])
        