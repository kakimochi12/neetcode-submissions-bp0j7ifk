class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevmap = set()

        for n in nums:
            if n in prevmap:
                return True
            prevmap.add(n)
        return False