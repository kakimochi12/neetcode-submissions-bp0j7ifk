class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posdiag = set()
        negdiag = set()

        board = [["."] * n for i in range(n)]

        res = []

        def dfs(r):
            if r == n:
                copy = ["".join(rows) for rows in board]
                res.append(copy)
                return res
            for c in range(n):
                if c in cols or r + c in posdiag or r-c in negdiag:
                    continue
                
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"

                dfs(r+1)

                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res