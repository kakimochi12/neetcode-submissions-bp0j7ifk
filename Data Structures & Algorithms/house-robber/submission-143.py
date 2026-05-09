class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        memo = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]
        return dfs(0)