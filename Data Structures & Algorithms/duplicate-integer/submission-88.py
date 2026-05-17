class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = set()

        for i in nums:
            if i in prevMap:
                return True
            prevMap.add(i)
        return False