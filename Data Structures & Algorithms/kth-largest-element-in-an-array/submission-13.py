class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        res = 0
        heapq.heapify(nums)
        while k > 0:
            res = -heapq.heappop(nums)
            k -= 1
        return res