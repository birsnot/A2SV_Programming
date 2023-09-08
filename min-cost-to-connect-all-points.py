class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        for i, p in enumerate(points):
            points[i] = tuple(p)

        N = len(points)           
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
            if pu == pv: return False
            if size[pu] > size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]
            return True
        
        costs = []
        for i, j in combinations(range(N), 2):
            x1, y1 = points[i]
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            costs.append((cost, i, j))

        costs.sort()
        ans = 0
        cnt = 0
        for c, i, j in costs:
            if union(i, j):
                cnt += 1
                ans += c
                if cnt == N - 1:
                    return ans
        return ans