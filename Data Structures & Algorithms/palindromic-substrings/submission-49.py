class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0

        dp = [[False] * (n) for i in range(n)]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i+1 <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1
        return res