class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for d in num:
            n = n*10 + d
        n += k
        return list(map(int, str(n)))