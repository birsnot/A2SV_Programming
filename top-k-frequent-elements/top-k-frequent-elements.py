class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        fr = [[] for _ in range(len(nums)+1)]
        for n, f in c.items():
            fr[f].append(n)
        ans = []
        i = len(nums)
        while len(ans) < k:
            for n in fr[i]:
                ans.append(n)
            i -= 1
        return ans
