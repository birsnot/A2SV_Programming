class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num[-1] += k
        c = 0
        N = len(num)-1
        for i in range(N, 0, -1):
            c, num[i] = divmod(num[i]+c, 10)
            if not c:
                break
        c, num[0] = divmod(num[0]+c, 10)
        if c: return list(map(int, str(c))) + num
        return num