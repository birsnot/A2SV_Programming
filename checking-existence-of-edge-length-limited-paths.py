class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        size = [1]*n

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
        
        edgeList.sort(key=lambda e: e[2])
        Q = len(queries)
        E = len(edgeList)
        qry_idx = sorted(range(Q), key=lambda i: queries[i][2])
        ans = [False]*Q
        i = 0
        for idx in qry_idx:
            u, v, limit = queries[idx]
            while i < E and edgeList[i][2] < limit:
                union(edgeList[i][0], edgeList[i][1])
                i += 1
            ans[idx] = find(u) == find(v)
        return ans