class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        indegree = [[0] * COLS for i in range(ROWS)]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS) and matrix[nr][nc] < matrix[r][c]):
                        indegree[r][c] += 1

        for r in range(ROWS):
            for c in range(COLS):
                if indegree[r][c] == 0:
                    q.append((r, c))
        LIS = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS) and matrix[nr][nc] > matrix[r][c]):
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append((nr, nc))
            LIS += 1
        return LIS
        
        