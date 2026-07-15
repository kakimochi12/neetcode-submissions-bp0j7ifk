class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def dfs(openN, closedN):
            if openN == closedN == n:
                res.append("".join(subset))
                return
            if openN < n:
                subset.append("(")
                dfs(openN + 1, closedN)
                subset.pop()
            if closedN < openN:
                subset.append(")")
                dfs(openN, closedN + 1)
                subset.pop()
        dfs(0, 0)
        return res