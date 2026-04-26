class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(a):
            if a in memo:
                return memo[a]
            if a == 0:
                return 0
            
            res = float("inf")
            for c in coins:
                if a-c >= 0:
                    res = min(res, 1 + dfs(a-c))
            memo[a] = res
            return res
        return dfs(amount) if dfs(amount)!= float("inf") else -1