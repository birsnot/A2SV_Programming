class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        opening = 0
        for ch in s:
            if ch == "(":
                opening += 1
            elif ch == "*":
                count += 1
            else:
                if opening: opening -= 1
                elif count: count -= 1
                else: return False
        count = 0
        closing = 0
        for ch in s[::-1]:
            if ch == ")":
                closing += 1
            elif ch == "*":
                count += 1
            else:
                if closing: closing -= 1
                elif count: count -= 1
                else: return False
        return True