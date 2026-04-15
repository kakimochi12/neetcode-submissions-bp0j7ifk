class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        
        memo = [[-1] * (half + 1) for i in range(len(nums)+1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            
            memo[i][target] = dfs(i+1, target) or dfs(i+1, target - nums[i])
            return memo[i][target]
        return dfs(0, half)