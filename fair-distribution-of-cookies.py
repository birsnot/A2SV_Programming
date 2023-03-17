class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        bucket = [0]*k
        for i, n in enumerate(cookies[::-1]):
            bucket[i%k] += n
        ans = max(bucket)
        bucket = [0]*k
        def backtrack(i):
            nonlocal ans
            if i >= len(cookies):
                ans = min(ans, max(bucket))
                return
            if max(bucket) >= ans:
                return
            for j in range(k):
                bucket[j] += cookies[i]
                backtrack(i+1)
                bucket[j] -= cookies[i]
        backtrack(0)
        return ans