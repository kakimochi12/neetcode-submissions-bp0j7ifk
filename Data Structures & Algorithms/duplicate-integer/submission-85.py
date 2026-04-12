class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevset = set()
        for n in nums:
            if n in prevset:
                return True
            prevset.add(n)
        return False