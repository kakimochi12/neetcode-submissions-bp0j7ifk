class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = set()
        for n in nums:
            if n in prevMap:
                return True
            prevMap.add(n)
        return False