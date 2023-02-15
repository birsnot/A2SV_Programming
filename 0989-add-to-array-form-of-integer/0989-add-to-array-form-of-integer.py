class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for d in num:
            n = n*10 + d
        n += k
        ans = []
        while n > 0:
            ans.append(n%10)
            n //= 10
        return ans[::-1]