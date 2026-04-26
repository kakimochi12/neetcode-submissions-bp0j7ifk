class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        memo = [[-1] * 2 for i in range(len(nums)+1)]
        
        def dfs(i, flag):
            if i >= len(nums) or (i == len(nums)-1 and flag):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i+1, flag), nums[i] + dfs(i+2, (flag or i == 0)))
            return memo[i][flag]
        return max(dfs(0, False), dfs(0, True))
            