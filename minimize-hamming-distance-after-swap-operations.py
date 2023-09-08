class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        N = len(source)
        parent = list(range(N))
        size = [1]*N

        def find(v):
            path = []
            while parent[v] != v:
                path.append(v)
                v = parent[v]
            for x in path:
                parent[x] = v
            return v
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv: return
            if size[pu] < size[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            size[pu] += size[pv]
        
        for u, v in allowedSwaps:
            union(u, v)
        cnt = {}
        for i in range(N):
            p = find(i)
            if p not in cnt:
                cnt[p] = defaultdict(int)
            cnt[p][source[i]] -= 1
            cnt[p][target[i]] += 1
        ans = 0
        for n in cnt:
            for fq in cnt[n].values():
                ans += (fq)*(fq > 0)
        return ans