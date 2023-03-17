class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        for c in combinations(range(1, n + 1) , k):
            ans.append(c)
        return ans