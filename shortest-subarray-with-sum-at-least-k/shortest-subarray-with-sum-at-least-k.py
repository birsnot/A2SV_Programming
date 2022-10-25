class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque([(-1,0)])
        sums = 0
        res = len(nums) + 1

        for i,n in enumerate(nums):
            sums += n
            if n > 0:
                target = sums-k
                while q and q[0][1] <= target:
                    res = min(res,i-q.popleft()[0])
            else:
                while q and sums <= q[-1][1]:
                    q.pop()
            q.append((i,sums))
        return -1 if res > len(nums) else res
