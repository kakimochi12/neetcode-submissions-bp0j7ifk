class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_str={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []

        def dfs(i, curstr):
            if len(curstr) == len(digits):
                res.append(curstr)
                return
            
            for c in digits_to_str[digits[i]]:
                dfs(i+1, curstr + c)
        
        if digits:
            dfs(0, "")
        return res