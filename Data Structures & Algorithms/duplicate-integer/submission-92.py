class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevmap = set()

        for i in nums:
            if i in prevmap:
                return True
            prevmap.add(i)
        return False