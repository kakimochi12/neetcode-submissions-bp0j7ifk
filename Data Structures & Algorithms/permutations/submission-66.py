class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res
    def backtrack(self, nums, i):
        if i >= len(nums):
            self.res.append(nums.copy())
            return
        
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.backtrack(nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]