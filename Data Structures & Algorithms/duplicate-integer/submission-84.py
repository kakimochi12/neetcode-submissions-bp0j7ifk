class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevset = set()

        for i in nums:
            if i in prevset:
                return True
            prevset.add(i)
        return False
        