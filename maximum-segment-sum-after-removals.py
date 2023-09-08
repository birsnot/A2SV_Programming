class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        N = len(nums)
        parent = list(range(N))
        value = [0]*(N + 1)
        max_ = 0

        def find(i):
            path = []
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for x in path:
                parent[x] = i
            return i

        ans = [0]*N
        for idx in range(N - 1, 0, -1):
            i = removeQueries[idx]
            value[i] = nums[i]
            p = i
            if value[i - 1] > 0:
                p = find(i - 1)
                parent[i] = p
                value[p] += value[i]
            if value[i + 1] > 0:
                pr = find(i + 1)
                parent[p] = pr
                value[pr] += value[p]
                p = pr
            max_ = max(max_, value[p])
            ans[idx - 1] = max_
        
        return ans