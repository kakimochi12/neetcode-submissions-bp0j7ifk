class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft, maxRight = 0, 0

        for i in s:
            if i == "(":
                minLeft += 1
                maxRight += 1
            elif i == ")":
                minLeft -= 1
                maxRight -= 1
            else:
                minLeft -= 1
                maxRight += 1
            if maxRight < 0:
                return False
            if minLeft < 0:
                minLeft = 0
        return minLeft == 0