class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = nums[0]

        for n in nums:
            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(res, curMax)
            
        return res