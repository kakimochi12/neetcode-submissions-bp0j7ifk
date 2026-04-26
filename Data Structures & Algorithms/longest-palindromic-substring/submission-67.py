class Solution:
    def longestPalindrome(self, s: str) -> str:
        index, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i+1 <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > resLen:
                        index = i
                        resLen = j - i + 1
        return s[index:index+resLen] 
