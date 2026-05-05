class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, total):
            if i >= len(nums):
                return 1 if target == total else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i])
            return dp[(i, total)]
        return dfs(0, 0)
            
