class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(r-l+1, res)
        return res