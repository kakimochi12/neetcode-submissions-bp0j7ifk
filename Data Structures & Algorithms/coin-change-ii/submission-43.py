class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)-1,-1, -1):
            newDP = [0] * (amount + 1)
            newDP[0] = 1
            for a in range(1, amount + 1):
                newDP[a] = dp[a]
                if a - coins[i] >= 0:
                    newDP[a] += newDP[a-coins[i]]
            dp = newDP
        return dp[amount]