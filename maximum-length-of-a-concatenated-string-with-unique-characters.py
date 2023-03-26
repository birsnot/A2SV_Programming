class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        N = len(arr)
        def helper(i, prev):
            nonlocal ans
            if i == N:
                if len(prev) > ans:
                    ans = len(prev)
                return
            cur = set(arr[i])
            if len(arr[i]) == len(cur) and prev.isdisjoint(cur):
                helper(i + 1, prev.union(cur))
            helper(i + 1, prev)
        helper(0, set())
        return ans