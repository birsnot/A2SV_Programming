class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        cur = 1
        def bt(mask):
            nonlocal cur, ans
            if cur == n + 1:
                ans += 1
                return
            for i in range(1, n + 1):
                if mask&(1<<i) == 0 and (i%cur == 0 or cur%i == 0):
                    cur += 1
                    bt(mask | (1<<i))
                    cur -= 1
        bt(0)
        return ans