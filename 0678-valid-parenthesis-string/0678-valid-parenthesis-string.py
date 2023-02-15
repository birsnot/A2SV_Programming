class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        for ch in s:
            if ch == ")":
                if count: count -= 1
                else: return False
            else: count += 1
        count = 0
        for ch in s[::-1]:
            if ch == "(":
                if count: count -= 1
                else: return False
            else: count += 1
        return True