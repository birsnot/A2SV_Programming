class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))

        def find(v):
            path = []
            while parent[v] != v:
                path.append(v)
                v = parent[v]
            for x in path:
                parent[x] = v
            return v

        hate = defaultdict(set)
        for x, y in restrictions:
            hate[x].add(y)
            hate[y].add(x)
        
        ans = []
        for u, v in requests:
            pu = find(u)
            pv = find(v)
            if pu == pv:
                ans.append(True)
            else:
                if pv in hate[pu]:
                    ans.append(False)
                else:
                    if len(hate[pu]) < len(hate[pv]):
                        pu, pv = pv, pu
                    hate[pu].update(hate[pv])
                    for x in hate[pv]:
                        hate[x].remove(pv)
                        hate[x].add(pu)
                    parent[pv] = pu
                    ans.append(True)
        return ans