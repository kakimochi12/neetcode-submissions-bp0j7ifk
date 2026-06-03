class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O" or (r, c) in visited):
                return
            visited.add((r, c))
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        grid = board

        for r in range(ROWS):
            if grid[r][0] == "O":
                dfs(r, 0)
            if grid[r][COLS-1] == "O":
                dfs(r, COLS-1)
        for c in range(COLS):
            if grid[0][c] == "O":
                dfs(0, c)
            if grid[ROWS-1][c] == "O":
                dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "O":
                    grid[r][c] = "X"
                elif grid[r][c] == "T":
                    grid[r][c] = "O"
